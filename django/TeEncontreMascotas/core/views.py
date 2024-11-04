from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, 'core/index.html') 

def base(request):
    return render(request, 'core/base.html')

def registro(request):
    return render(request, 'core/registro.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')

def login(request):
    return render(request, 'core/login.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def recuperar_contrasena(request):
    return render(request, 'core/recuperar_contrasena.html')