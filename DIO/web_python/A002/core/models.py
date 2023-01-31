from django.db import models


# Create your models here
class Eventos(models.Model):
    titulo = models.CharField(max_length=100) #limite que ele tera, ou seja no maximo 100 caracteristicas
    descrição = models.TextField(blank=True, null=True) #usado para funcao que nao tenha limite de caracter

    data_evento = models.DateTimeField()
    data_criação = models.DateTimeField(auto_now=True) #esta data tem que ser automatica e nao pode ser alterada pelo usuario, ou seja, assim que o usuario criar um evento, ira gerar uma data de criação a qual referece ao dia de criacao do mesmo.
    
    
    
    '''     FUNCOES PARA MIGRAR A TABELA NO DJANGO
    
    python manage.py makemigrations nome_do_projeto
    '''