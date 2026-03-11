from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.db.models import Count
from django.utils import timezone
from .models import Enquete, Opcao, Voto, Usuario
from .forms import RegistoForm, LoginForm, EnqueteForm

def landing_page(request):
    return render(request, 'votos/landing.html')

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Conta criada com sucesso para {user.nome}!")
            if not request.user.is_authenticated:
                # Se não havia ninguém logado, loga o novo utilizador
                login(request, user)
            return redirect('lista_enquetes')
    else:
        form = RegistoForm(user=request.user)
    return render(request, 'votos/registo.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.nome}!")
            return redirect('lista_enquetes')
    else:
        form = LoginForm()
    return render(request, 'votos/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Sessão terminada.")
    return redirect('landing_page')

def lista_enquetes(request):
    agora = timezone.now()
    q = request.GET.get('q', '')
    
    enquetes_ativas = Enquete.objects.filter(
        dataInicio__lte=agora,
        dataFim__gte=agora,
        status='ativa'
    )
    
    enquetes_encerradas = Enquete.objects.filter(
        models.Q(dataFim__lt=agora) | models.Q(status='encerrada')
    )
    
    if q:
        enquetes_ativas = enquetes_ativas.filter(
            models.Q(titulo__icontains=q) | models.Q(descricao__icontains=q)
        )
        enquetes_encerradas = enquetes_encerradas.filter(
            models.Q(titulo__icontains=q) | models.Q(descricao__icontains=q)
        )
        
    enquetes_ativas = enquetes_ativas.order_by('-dataInicio')
    enquetes_encerradas = enquetes_encerradas.order_by('-dataFim')
    
    return render(request, 'votos/lista.html', {
        'enquetes': enquetes_ativas,
        'enquetes_encerradas': enquetes_encerradas,
        'agora': agora,
        'q': q
    })

@login_required
@login_required
def detalhe_enquete(request, pk):
    enquete = get_object_or_404(Enquete, pk=pk)
    voto_utilizador = Voto.objects.filter(usuario=request.user, enquete=enquete).first()
    
    # Se a enquete terminou, se o utilizador já votou, ou se é admin, mostra resultados
    mostrar_resultados = enquete.dataFim < timezone.now() or voto_utilizador or enquete.status == 'encerrada' or request.user.tipo == 'admin'
    
    resultados = None
    if mostrar_resultados:
        from django.db.models import Count
        resultados = enquete.opcoes.annotate(voto_count=Count('voto')).order_by('-voto_count')

    if request.method == 'POST':
        if request.user.tipo == 'admin':
            messages.error(request, "Administradores não podem votar.")
            return redirect('detalhe_enquete', pk=pk)
        
        if voto_utilizador:
            messages.warning(request, "Já votou nesta enquete.")
            return redirect('detalhe_enquete', pk=pk)
        
        if not enquete.is_active():
            messages.error(request, "Esta enquete não está ativa.")
            return redirect('lista_enquetes')

        opcao_id = request.POST.get('opcao')
        if not opcao_id:
            messages.error(request, "Selecione uma opção.")
            return redirect('detalhe_enquete', pk=pk)
        
        opcao = get_object_or_404(Opcao, id=opcao_id, enquete=enquete)
        
        # Registar Voto atomicamente
        from django.db.models import F
        from django.db import transaction
        
        with transaction.atomic():
            Voto.objects.create(usuario=request.user, enquete=enquete, opcao=opcao)
            Opcao.objects.filter(id=opcao_id).update(quantidadeVotos=F('quantidadeVotos') + 1)
            # Remover atualização manual de Resultado, será calculado por agregação
        
        messages.success(request, "Voto registado com sucesso!")
        return redirect('detalhe_enquete', pk=pk)

    return render(request, 'votos/detalhe.html', {
        'enquete': enquete,
        'mostrar_resultados': mostrar_resultados,
        'resultados': resultados,
        'voto_utilizador': voto_utilizador,
        'agora': timezone.now()
    })

@login_required
def criar_enquete(request):
    if request.user.tipo != 'admin':
        messages.error(request, "Apenas administradores podem criar enquetes.")
        return redirect('lista_enquetes')
    
    if request.method == 'POST':
        form = EnqueteForm(request.POST)
        if form.is_valid():
            enquete = form.save(commit=False)
            enquete.usuario = request.user
            enquete.save()
            
            for texto in form.cleaned_data['opcoes_lista']:
                Opcao.objects.create(enquete=enquete, descricao=texto, quantidadeVotos=0)
            
            messages.success(request, "Enquete criada com sucesso!")
            return redirect('lista_enquetes')
    else:
        form = EnqueteForm()
    return render(request, 'votos/criar_enquete.html', {'form': form})

@login_required
def cancelar_enquete(request, pk):
    if request.user.tipo != 'admin':
        messages.error(request, "Acesso negado.")
        return redirect('lista_enquetes')
    
    enquete = get_object_or_404(Enquete, pk=pk)
    enquete.status = 'encerrada'
    enquete.save()
    messages.warning(request, "Enquete encerrada.")
    return redirect('lista_enquetes')

@login_required
def apagar_enquete(request, pk):
    if request.user.tipo != 'admin':
        messages.error(request, "Acesso negado.")
        return redirect('lista_enquetes')
    
    enquete = get_object_or_404(Enquete, pk=pk)
    if request.method == 'POST':
        enquete.delete()
        messages.success(request, "Enquete eliminada permanentemente.")
        return redirect('lista_enquetes')
@login_required
def lista_utilizadores(request):
    if request.user.tipo != 'admin':
        messages.error(request, "Acesso negado.")
        return redirect('lista_enquetes')
    
    utilizadores = Usuario.objects.all().order_by('nome')
    return render(request, 'votos/utilizadores.html', {'utilizadores': utilizadores})
