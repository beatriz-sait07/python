from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

'''
modelo 1, modelo 2 fica na views
def index(request):
    return redirect('/agenda/')  #mode de redirecionamento caso voce tenha um parameto de url/index vazio
'''
def lista_eventos(request):
    #evento = Evento.objects.get(id=1) --> busca apenas um elemento 'aquele que foi requesitado'
    usuario = request.user
    evento = Evento.objects.all() # faz uma listagem dos objetos
    #evento = Evento.objects.filter(usuario=usuario) # filta na pagina html a aparecer apenas os dados do usuario que esta logado no momento
    response = {'eventos': evento}
    return render(request, 'agenda.html', response) #renderizar a pagina html