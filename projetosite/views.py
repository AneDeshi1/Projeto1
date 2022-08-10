from django.shortcuts import render


def home(request):
    return render(request, 'projetosite/home.html', context={
        'name': 'Pedro Leite '
    })


# Create your views here.
