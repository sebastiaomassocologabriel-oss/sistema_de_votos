from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('registo/', views.registo_view, name='registo'),
    path('utilizadores/', views.lista_utilizadores, name='lista_utilizadores'),
    path('entrar/', views.login_view, name='login'),
    path('sair/', views.logout_view, name='logout'),
    path('enquetes/', views.lista_enquetes, name='lista_enquetes'),
    path('enquetes/<int:pk>/', views.detalhe_enquete, name='detalhe_enquete'),
    path('enquetes/criar/', views.criar_enquete, name='criar_enquete'),
    path('enquetes/<int:pk>/cancelar/', views.cancelar_enquete, name='cancelar_enquete'),
    path('enquetes/<int:pk>/apagar/', views.apagar_enquete, name='apagar_enquete'),
]
