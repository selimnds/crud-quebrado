from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.CriarVaga.as_view(), name='criar_vaga'),
    path('listar/', views.ListaVaga.as_view(), name='listar_vaga'),
    path('editar/<int:pk>/', views.EditarVaga.as_view(), name='editar_vaga'),
    path('apagar/<int:pk>/', views.ApagarVaga.as_view(), name='apagar_vaga'),
    path('detail/<int:pk>/', views.DetalheVaga.as_view(), name='detalhes_vaga'),   
    path('candidato/<int:pk>/', views.Candidato.as_view(), name='candidatos'),   
    
]