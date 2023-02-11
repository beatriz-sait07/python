from django.shortcuts import render
from core.models import Evento

# Create your views here.
def lista_eventos(request):
    #evento = Evento.objects.get(id=1) --> busca apenas um elemento 'aquele que foi requesitado'
    evento = Evento.objects.all() # faz uma listagem dos objetos
    response = {'eventos': evento}
    return render(request, 'agenda.html', response) #renderizar a pagina html