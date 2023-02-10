from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #limite maximo de caracter
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True) #feito para que o usuario nao modifique o mesmo, e ele eh gerado no momento da criacao do evento
    
    class Meta:
        db_table = 'evento'
        
    def __str__(self):
        return self.titulo