from django.db import models

# Create your models here.
class Vagas (models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=500)
    
    def __str__(self):
        return self.titulo
    
class Candidatos (models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome

    