from django.urls import path

from projetosite.views import home

urlpatterns = [
    path('', home),
]
