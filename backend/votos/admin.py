from django.contrib import admin
from .models import Usuario, Enquete, Opcao, Voto

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'tipo', 'is_staff')
    list_filter = ('tipo', 'is_staff')
    search_fields = ('nome', 'email')

    # do not allow creating new users through the admin site
    def has_add_permission(self, request):
        # only allow adding if you really need it; returning False hides the "Add" button
        return False

    # optionally, prevent elevation of existing users to superuser via admin form
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and obj.is_superuser:
            # non-superusers should not be able to mark someone as superuser
            obj.is_superuser = False
        super().save_model(request, obj, form, change)

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 3

@admin.register(Enquete)
class EnqueteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'dataInicio', 'dataFim', 'status')
    list_filter = ('status', 'dataInicio')
    search_fields = ('titulo', 'descricao')
    inlines = [OpcaoInline]

@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'enquete', 'opcao', 'dataVoto')
    list_filter = ('enquete',)
