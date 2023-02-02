from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here
class Eventos(models.Model):
    titulo = models.CharField(max_length=100) #limite que ele tera, ou seja no maximo 100 caracteristicas
    descrição = models.TextField(blank=True, null=True) #usado para funcao que nao tenha limite de caracter

    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criação = models.DateTimeField(auto_now=True) #esta data tem que ser automatica e nao pode ser alterada pelo usuario, ou seja, assim que o usuario criar um evento, ira gerar uma data de criação a qual referece ao dia de criacao do mesmo.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #ON-DELETE: caso o usuario seja 'excluido' todas as coisas criada por ele será excluidas juntos
    
    class Meta:
        db_table = 'evento'
        
    def __str__(self):
        return self.titulo
    
    def get_data_criacao(self):
        return self.data_evento.strftime('%d/%m/%Y - %H:%M Hr') #mudando o formato da data que esta dentro do html
    
    '''     FUNCOES PARA MIGRAR A TABELA NO DJANGO
    ***obs:  cada migracao ira criar um novo arquiva, entao tenta sempre fazer a migração dos dados
    e arquivos necessarios.
    geralmente os novos atributos de arquivos utiliza-se o nome da pasta e suas caracteristica anterios, caso deseje mudar usar a classe Meta.
    ***
    
    
    comando:
    
    
    1 - python manage.py makemigrations nome_do_projeto
    
    2 - python manage.py sqlmigrate core
    
    3 - 
    
    '''