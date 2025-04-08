from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.CriarVaga.as_view(), name='criar_vaga'),
    path('listar/', views.ListaVaga.as_view(), name='listar_vaga'),
    path('<int:pk>/editar/', views.EditarVaga.as_view(), name='editar_vaga'),
    path('<int:pk>/apagar/', views.ApagarVaga.as_view(), name='apagar_vaga'),
    
]