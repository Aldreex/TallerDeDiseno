from django.contrib import admin
from .models import *
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = [ 'id_mascota', 'nombre', 'edad', 'especie', 'raza', 'ubicacion', 'estado']
    search_fields = ['nombre', 'especie', 'estado']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id_usuario', 'nombre', 'apellido', 'correo', 'edad', 'direccion', 'ciudad', 'fono']
    search_fields = ['nombre', 'apellido', 'correo', 'edad', 'direccion', 'ciudad', 'fono']

class FavoritosAdmin(admin.ModelAdmin):
    list_display = ("id_usuario", "consegir_mascotas")
    search_fields = ["id_usuario", "consegir_mascotas"]

    def consegir_mascotas(self, obj):
        return "\n".join([str(mascota.id_mascota) for mascota in obj.id_mascota.all()])


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['id_publicacion','id_mascota', 'id_usuario', 'estado', 'fecha_publicacion']
    search_fields = ['id_mascota', 'id_usuario', 'estado', 'fecha_publicacion']
    

class MensajeAdmin(admin.ModelAdmin):
    list_display = ['id_mensaje', 'id_remitente',  'id_publicacion', 'contenido','fecha_envio']
    search_fields = ['id_remitente', 'id_publicacion', 'contenido', 'fecha_envio']

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Favoritos, FavoritosAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Mensaje, MensajeAdmin)

