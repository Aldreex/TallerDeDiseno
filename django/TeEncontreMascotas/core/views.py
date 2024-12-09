from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from  django.core.exceptions import *
from .models import *
from .forms import *
import datetime 
import json

# Create your views here.
def index(request):
    correo = request.session.get("correo", "Invitado")
    is_logged_in = request.session.get("is_logged_in", False)
    
    if is_logged_in:
        return TemplateResponse(request, "core/index.html", {correo: correo})
    
    return TemplateResponse(request, 'core/index.html') 

def base(request):
    fecha = request.session["fecha"] = datetime.date.today()
    correo = request.session.get("correo", "Invitado")
    is_logged_in = request.session.get("is_logged_in", False)
    if is_logged_in:
        return TemplateResponse(request, "core/base.html", {correo: correo})

    return TemplateResponse(request, 'core/base.html', {correo: correo})


def catalogo(request):    
    listaMascotas = Mascota.objects.all()
    datos = {
        "listaMascotas" : listaMascotas
    }
    
    return TemplateResponse(request, 'core/catalogo.html', datos)

def login(request):
    sesionIniciada = request.session.get("is_logged_in", False)
    if request.method == 'POST' and not sesionIniciada:
        form = LoginForm(request.POST)
        if form.is_valid():
            correoIn = form.cleaned_data["correo"]
            passIn = form.cleaned_data["contrasenia"]
            try: 
                usuario = Usuario.objects.get(correo=correoIn, contrasenia = passIn)
                request.session["nombre"] = usuario.nombre
                request.session["correo"] = correoIn
                request.session["is_logged_in"] = True
                request.session["id"] = usuario.id_usuario
                print("Sesion Iniciada con Exito")
                return TemplateResponse(request, 'core/index.html', {"correo": correoIn})
            except:
                return TemplateResponse(request, 'core/login.html', {"form":LoginForm()})

    else:
        form = LoginForm()

    return TemplateResponse(request, 'core/login.html', {"form":form})

def logout(request):
    request.session.flush()
    return TemplateResponse(request, 'core/index.html', {})

def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            correoIn = form.cleaned_data["correo"]
            
            try: 
                _ = Usuario.objects.get(correoIn)
                return HttpResponseRedirect("/")
            except:
                form.save()
                return HttpResponseRedirect("/login")
        else:
            return HttpResponse("/")    
    else:
        form = RegisterForm()
    

    return TemplateResponse(request, 'core/registro.html', {"form":form})

def servicios(request):
    return TemplateResponse(request, 'core/servicios.html')

def agregarMascota(request):
    if request.method == 'POST':
        form =MascotaForm(request.POST)
        if form.is_valid():
            correoSesion = request.session["correo"]
            usuario = Usuario.objects.get(correo=correoSesion)
    
            nuevaMascota=  form.save(commit=False)
            nuevaMascota.id_usuario = usuario
            print("fecha: ", datetime.date.today())
            nuevaMascota.fecha_registro = str(datetime.date.today())

            try:
                nuevaMascota.save()
                
                return TemplateResponse(request, 'core/index.html', {})
            except ModuleNotFoundError:
                
                return TemplateResponse(request, "core/index.html", {})
        else:
            return TemplateResponse(request, "core/index.html", {})

    form = MascotaForm()

    return TemplateResponse(request, 'core/mascotas/agregarmascota.html', {"form": form})

def recuperar_contrasena(request):

    if request.method == 'POST':
        form = RecuperarContrasenaForm(request.POST)
        if form.is_valid():
            rutIn = form.cleaned_data["rut"]
            try:
                usuario = Usuario.objects.get(rut=rutIn)
                ## aqui enviar mail a usuario
                print("Contraseña :", usuario.contrasenia)
                return HttpResponseRedirect("/")
            except:
                print("No se encontro el usuario")
                form = RecuperarContrasenaForm()
                return TemplateResponse(request, 'core/recuperar_contrasena.html', {"form": form})
        else:
            print("Formulario Invalido")
            return HttpResponseRedirect("/recuperar_contrasena")
    else:
        form = RecuperarContrasenaForm()

    return TemplateResponse(request, 'core/recuperar_contrasena.html', {"form":form})