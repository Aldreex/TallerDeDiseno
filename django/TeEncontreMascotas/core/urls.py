from django.urls import path 
from .views import * 
 
urlpatterns = [ 
   path("", index, name="index"),
   path("registro/", registro, name="registro"),
   path("catalogo/", catalogo, name="catalogo"),
   path("login/", login, name="login"),
   path("servicios/", servicios, name="servicios"),
   path("recuperar_contrasena", recuperar_contrasena, name="recuperar_contrasena"),
   path("mascotas/agregarmascota/", agregarMascota, name="agregarmascota"),
   path("logout", logout, name="logout" ),
   path("guardarFavorito", guardarFavorito, name="guardarFavorito" ),
   path("eliminarFavorito", eliminarFavorito, name="eliminarFavorito"),
   path("conseguirDetalle", conseguirDetalle, name="conseguirDetalle"),
   path("crearComunas", crearComunas, name="crearComunas")
] 
