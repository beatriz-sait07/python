from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

'''
modelo 1, modelo 2 fica na views
def index(request):
    return redirect('/agenda/')  #mode de redirecionamento caso voce tenha um parameto de url/index vazio
'''

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
    else:
        redirect('/')

@login_required(login_url='/login/') #se voce nao estiver autenticado, ele não liverarpa a agenda
    
def lista_eventos(request):
    #evento = Evento.objects.get(id=1) --> busca apenas um elemento 'aquele que foi requesitado'
    usuario = request.user
    evento = Evento.objects.all() # faz uma listagem dos objetos
    #evento = Evento.objects.filter(usuario=usuario) # filta na pagina html a aparecer apenas os dados do usuario que esta logado no momento
    response = {'eventos': evento}
    return render(request, 'agenda.html', response) #renderizar a pagina html