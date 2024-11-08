from django.contrib import admin
from .models import *
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = [ 'id_mascota', 'nombre', 'edad', 'especie', 'raza', 'ubicacion', 'estado']
    search_fields = ['nombre', 'especie', 'estado']
    list_per_page = 2

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id_usuario', 'nombre', 'apellido', 'correo', 'edad', 'direccion', 'ciudad', 'fono']
    search_fields = ['nombre', 'apellido', 'correo', 'edad', 'direccion', 'ciudad', 'fono']

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['id_publicacion','id_mascota', 'id_usuario', 'estado', 'fecha_publicacion']
    search_fields = ['id_mascota', 'id_usuario', 'estado', 'fecha_publicacion']
    

class MensajeAdmin(admin.ModelAdmin):
    list_display = ['id_mensaje', 'id_remitente', 'id_destinatario', 'id_publicacion', 'fecha_envio']
    search_fields = ['id_remitente', 'id_destinatario', 'id_publicacion', 'fecha_envio']

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Mensaje, MensajeAdmin)

