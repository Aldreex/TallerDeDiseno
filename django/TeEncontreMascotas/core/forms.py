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
            'fono',
            'comuna'
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
            ),
            "comuna": forms.HiddenInput()
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
            "imagen"
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"label": "Nombre", "class": "form-control", "required": True}),
            "edad": forms.NumberInput(attrs={"class": "form-control", "required": True}),
            "especie": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "raza": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "descripcion": forms.TextInput(attrs={"class": "form-control", "cols":110, "required": True}),
            "ubicacion": forms.TextInput(attrs={"class": "form-control", "required": True}),  
            "estado" : forms.HiddenInput(),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"})
        }

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
            'id_publicacion'
        ]
