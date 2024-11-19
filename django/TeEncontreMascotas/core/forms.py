from django import forms
from django.forms import ModelForm
from .models import *

class MascotaForm(ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'nombre', 
            'edad', 
            'especie', 
            'raza', 
            'descripcion', 
            'ubicacion', 
            'estado'
        ]
        
class LoginForm(ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'correo',
            'contrasenia'
        ]
        widgets = {
            "correo" : forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "required": True}
            ),
            'contrasenia' : forms.PasswordInput(
                attrs={
                "label":"Contraseña",
                "required" : True
                })
        }

class RegisterForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'correo',
            'contrasenia',
            'direccion',
            'edad',
            'ciudad',
            'fono'
        ] 
        widgets = {
            "nombre" : forms.TextInput(
                attrs={
                    "class":"form-control",
                    "id":"txtNombre",
                "required" : True

                }
            ),
            "apellido" : forms.TextInput(
                attrs={
                    "class":"form-control",
                "required" : True
                    
                }
            ),            
            "correo" : forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "id" : "txtCorreo",
                    "required" : True

                }
            ),
            "contrasenia" : forms.PasswordInput(
                attrs={
                    "class":"form-control",
                    "required" : True

                }
            ),            
            "direccion" : forms.TextInput(
                attrs={
                    "class":"form-control",
                    "required" : True

                }
            ),
            "ciudad" : forms.TextInput(
                attrs={
                    "class":"form-control",
                    "required" : True

                }
            ),            
            "edad" : forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "required" : True

                }
            ),
            "fono" : forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "required" : True

                }
            )
        }
        
class AgregarMascota(ModelForm):
    class Meta:
        model = Mascota
        fields = [
            "nombre",
            "edad",
            "especie",
            "raza",
            "descripcion",
            "ubicacion",
            "estado",
        ]

class RecuperarContrasenaForm(ModelForm):

    class Meta:
        model = Usuario
        fields = [
            "rut"
        ]
        widgets = {
            "rut" : forms.PasswordInput(
                attrs = {
                    "class" : "form-control",
                    "required" : True
                }

            )
        }

class MensajeForm(ModelForm):
    
    class Meta:
        model = Mensaje
        fields = [
            'publicacion'
        ]
