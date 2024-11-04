from django.urls import path 
from .views import * 
 
urlpatterns = [ 
   path("", index, name="index"),
   path("registro/", registro, name="registro"),
   path("catalogo/", catalogo, name="catalogo"),
   path("login/", login, name="login"),
   path("servicios/", servicios, name="servicios"),
   path("recuperar_contrasena", recuperar_contrasena, name="recuperar_contrasena")
] 
