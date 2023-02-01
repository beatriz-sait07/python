from django.shortcuts import render

#create u views here

def lista_eventos(request):
    return render(request, 'agenda.html')