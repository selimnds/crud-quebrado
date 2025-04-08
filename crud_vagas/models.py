from django.db import models

# Create your models here.
class Vagas (models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=500)
    
    def get_absolute_url(self): # new
        return reverse('lawyer_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.titulo