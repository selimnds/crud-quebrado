from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Vagas , Candidatos 
from django.core.mail import send_mail

# Create your views here.
class CriarVaga(CreateView):
    model = Vagas
    fields = ['titulo', 'descricao']
    template_name = 'crud_vagas/criar_vaga.html'
    success_url = '/listar/'
    #adc template ^^^^^^

class ListaVaga(ListView):
    model = Vagas
    context_object_name = 'vagas'
    template_name = 'crud_vagas/listar_vaga.html'
    #adc template ^^^^^^
    
class DetalheVaga(DetailView):
    model = Vagas
    template_name = "crud_vagas/detalhes_vaga.html"
    context_object_name = "vaga"
    
class EditarVaga(UpdateView):
    model = Vagas
    fields = ['titulo', 'descricao']
    template_name = 'crud_vagas/editar_vaga.html'
    success_url = '/listar/'

class ApagarVaga(DeleteView):
    model = Vagas
    fields = ['titulo', 'descricao']
    template_name = 'crud_vagas/apagar_vaga.html'
    context_object_name = "vaga"
    success_url = '/listar/'
    
class Candidato(CreateView):
    model = Candidatos
    fields = ['nome', 'email', 'telefone', 'cpf']
    template_name = 'crud_vagas/candidatacao.html'
    success_url = '/listar/'

    def form_valid(self, form):
        # Salva o candidato no banco de dados
        response = super().form_valid(form)

        send_mail(
            'teste',
            f'Novo candidato cadastrado:\n\nNome: {form.cleaned_data["nome"]}\nE-mail: {form.cleaned_data["email"]}\nTelefone: {form.cleaned_data["telefone"]}\nCPF: {form.cleaned_data["cpf"]}'
            'luizh.selim@gmail.com',  
            ['luizh.selim@gmail.com'],  
            fail_silently=False,  
        )   

        return response