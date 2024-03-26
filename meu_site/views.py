from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,"meu_site/inicio.html", {'pagina_ativa': 'inicio'})

def personagens(request):
    return render(request,"meu_site/rotas/personagens.html", {'pagina_ativa': 'personagens'})

def sobre(request):
    return render(request,"meu_site/rotas/sobre.html", {'pagina_ativa': 'sobre'})

def menu(request):
    return render(request,"meu_site/rotas/menu.html")

