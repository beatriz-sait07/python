from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #limite maximo de caracter
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True) #feito para que o usuario nao modifique o mesmo, e ele eh gerado no momento da criacao do evento
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #cascade serve para deletar TODOS os dados do usuario caso ele seja removido da lista
    
    class Meta:
        db_table = 'evento'
        
    def __str__(self):
        return self.titulo
    
    #a cada modificacao de classe, tu precisa migrar o banco de dados!