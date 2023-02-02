from django.shortcuts import render
from core.models import Eventos

#create u views here

def lista_eventos(request):
    usuario = Eventos.objects.all()
    evento = Eventos.objects.filter(usuario=usuario) #.get(seleciona o que deseja)
    # .all() aparece todos os eventos de todos usuarios
    dados = {'eventos': evento}
    return render('agenda.html', request, dados)