from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'projetosite/home.html', context={
        'name': 'Pedro Leite '
    })


def contato(request):
    return render(request, 'temp.html')


def sobre(request):
    return HttpResponse('sobre 3')
# Create your views here.
