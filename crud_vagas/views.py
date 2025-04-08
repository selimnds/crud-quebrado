from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vagas
# Create your views here.
class CriarVaga(CreateView):
    model = Vagas
    fields = ['titulo', 'descricao']
    template_name = 'crud_vagas/criar_vaga.html'
    #adc template ^^^^^^

class ListaVaga(ListView):
    model = Vagas
    context_object_name = 'vagas'
    template_name = ''
    #adc template ^^^^^^
    
class EditarVaga(UpdateView):
    model = Vagas
    template_name_suffix = '_upt'
    fields = ['titulo', 'descricao']
    
class ApagarVaga(DeleteView):
    model = Vagas
    fields = ['titulo', 'descricao']
    