from django.urls import path
from meu_site.views import inicio, sobre, personagens, menu

urlpatterns = [
    path('', inicio, name='inicio'),
    path('personagens/', personagens, name='personagens'),
    path('sobre/', sobre, name='sobre'),
    path('menu/', menu, name='menu'),
]