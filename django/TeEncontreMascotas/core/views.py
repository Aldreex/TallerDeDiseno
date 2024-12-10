from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
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
    fecha = datetime.date.today().isoformat()
    request.session["fecha"] = fecha
    correo = request.session.get("correo", "Invitado")
    is_logged_in = request.session.get("is_logged_in", False)
    if is_logged_in:
        return TemplateResponse(request, "core/base.html", {correo: correo})

    return TemplateResponse(request, 'core/base.html', {correo: correo})


def catalogo(request):    
    sesionIniciada = request.session.get("is_logged_in", False)
    comunas = Comuna.objects.all()
    listaMascotas = Mascota.objects.all()
    datos = {
        "listaMascotas": listaMascotas,
        "comunas" : comunas
    }
    datos["sesionIniciada"] = sesionIniciada
    mascotasFavoritas = []
    datos["estado_favoritos"] = 0
    
    
    if request.method == 'POST':
        comuna_sel = request.POST.get("filtroComuna", None)
        print(request.POST)
        if comuna_sel and comuna_sel != "todas":
            personas = Usuario.objects.filter(comuna = comuna_sel) 
            listaMascotas = Mascota.objects.select_related("id_usuario__comuna").filter(id_usuario__comuna = comuna_sel)
        estado_sel = request.POST.get("filtroTipo", None)
        if estado_sel and estado_sel != "todos":
            listaMascotas = listaMascotas.filter(estado = estado_sel)
        datos["listaMascotas"] = listaMascotas
    
    if sesionIniciada: 
        id_usuario = request.session.get("id", None)
        datos["id_usuario"] = id_usuario
        if id_usuario:
            
            try:
                favoritos = Favoritos.objects.get(id_usuario = id_usuario)
                datos["favs"] = favoritos.id_mascota.all()
                if(datos["favs"].exists()):
                   datos["estado_favoritos"] = 1
                else:
                    datos["estado_favoritos"] = 0
           
            except:
                
                datos["estado_favoritos"] = -1

    datos["favoritos"] = mascotasFavoritas
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
                request.session["nombre"] = usuario.nombre.capitalize()
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
    comunas = Comuna.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        comuna = request.POST.get("comuna")
        if form.is_valid() and comuna:
            correoIn = form.cleaned_data["correo"]
            nuevoUsuario = form.save(commit=False)
            comuna_seleccionada = Comuna.objects.get(id_comuna = comuna)
            nuevoUsuario.comuna = comuna_seleccionada

            try: 
                _ = Usuario.objects.get(correoIn)
                return HttpResponseRedirect("/")
            except:
                nuevoUsuario.save()
                return HttpResponseRedirect("/login")
        else:
            return HttpResponse("/")    
    else:
        form = RegisterForm()
    

    return TemplateResponse(request, 'core/registro.html', {"form":form, "comunas" : comunas})

def servicios(request):
    return TemplateResponse(request, 'core/servicios.html')

def agregarMascota(request):
    if request.method == 'POST':
        form =AgregarMascota(request.POST, request.FILES)
        
        if form.is_valid():
            correoSesion = request.session["correo"]
            usuario = Usuario.objects.get(correo=correoSesion)
    
            nuevaMascota=  form.save(commit=False)
            print(nuevaMascota.imagen)
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

    form = AgregarMascota()

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

def guardarFavorito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_usuario_in = data.get("id_usuario")
        id_mascota_in = data.get("id_mascota")
        usuario = Usuario.objects.get(id_usuario = id_usuario_in)
        mascota = Mascota.objects.get(id_mascota = id_mascota_in)
        
        try:
            favoritos = Favoritos.objects.get(id_usuario = id_usuario_in)
            favoritos.id_mascota.add(mascota)    
        except ObjectDoesNotExist:
            favoritos = Favoritos.objects.create(id_usuario = usuario)
            favoritos.id_mascota.add(mascota)
            
        try:
            favoritos.save()
            return JsonResponse({"message" : "ok"})
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON", "details": str(e)}, status=400)

    else:
        return TemplateResponse(request, 'core/catalogo.html')

def eliminarFavorito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_usuario_in = data.get("id_usuario")
        id_mascota_in = data.get("id_mascota")
        mascota = Mascota.objects.get(id_mascota = id_mascota_in)
        try:
            favoritos = Favoritos.objects.get(id_usuario = id_usuario_in)
            favoritos.id_mascota.remove(mascota)
            return JsonResponse({"message": "ok"})
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON", "details": str(e)}, status=400)
        
def conseguirDetalle(request):
    if request.method == 'GET':
        id_mascota_req = request.GET.get("id_mascota")
        try:
            mascota = Mascota.objects.get(id_mascota = id_mascota_req)
            fono = mascota.id_usuario.fono
            nombre = mascota.nombre
            especie = mascota.especie
            estado = mascota.estado
            descripcion = mascota.descripcion
            urlImagen= mascota.imagen.url
            return JsonResponse({
                "message": "OK", 
                "fono": fono,
                "nombre" : nombre,
                "especie" : especie,
                "estado" : estado,
                "descripcion" : descripcion,
                "urlImagen" : urlImagen
            }, status=200)
        except:

            return JsonResponse({"message": "No hay tal mascota"}, status=204)
        
def crearComunas(request):
    comunas = (
        "Alhué",
        "Buin",
        "Calera de Tango",
        "Cerrillos",
        "Cerro Navia",
        "Colina",
        "Conchalí",
        "Curacaví",
        "El Bosque",
        "Estación Central",
        "Huechuraba",
        "Independencia",
        "La Cisterna",
        "La Florida",
        "La Granja",
        "La Pintana",
        "La Reina",
        "Lampa",
        "Las Condes",
        "Lo Barnechea",
        "Lo Espejo",
        "Lo Prado",
        "Macul",
        "Maipú",
        "Melipilla",
        "Ñuñoa",
        "Padre Hurtado",
        "Paine",
        "Peñaflor",
        "Peñalolén",
        "Pirque",
        "Providencia",
        "Pudahuel",
        "Puente Alto",
        "Quilicura",
        "Quinta Normal",
        "Recoleta",
        "Renca",
        "San Bernardo",
        "San Joaquín",
        "San José de Maipo",
        "San Miguel",
        "San Pedro",
        "San Ramón",
        "Santiago",
        "Talagante",
        "Tiltil",
        "Vitacura"
    )

    comunadb = [Comuna(nombre = comuna) for comuna in comunas]
    print(comunadb)
    Comuna.objects.bulk_create(comunadb)
    return TemplateResponse(request, "core/index.html")