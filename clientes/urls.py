
from django.urls import path
from . import views

app_name = 'cliente'  # Namespace

urlpatterns = [
    path('', views.login_view, name='login'),  # Página inicial redirecionada para o login
    path('listar/', views.listar_clientes, name='listar_clientes'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
    path('login/', views.login_view, name='login'),  # Pode ser removida ou mantida
    path('cadastro/', views.cadastro, name='cadastro'),
]
