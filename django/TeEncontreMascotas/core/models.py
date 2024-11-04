from django.db import models

# Create your models here.
class Mascota(models.Model):
    
    id_mascota = models.AutoField("id_mascota", primary_key=True)
    nombre = models.CharField("Nombre Mascota", max_length=64)
    edad = models.IntegerField("Edad Mascota", null=True)
    especie = models.CharField("Especie Mascota", max_length=32)
    raza = models.CharField("Raza Mascota", max_length=32, null=True)
    descripcion = models.TextField("Descripcion Mascota", max_length=254)
    ubicacion = models.CharField("Ubicacion Mascota", max_length=64)
    estado = models.CharField("Estado Mascota", max_length=20, null=True)
    fecha_registro = models.DateField("Fecha de Registro")

    def __str__(self):
        return f"Mascota {self.nombre}"

class Usuario(models.Model):
    id_usuario = models.AutoField(verbose_name="Id de Usuario", primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    contrasenia = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    fono = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Publicacion(models.Model):
    id_publicacion = models.AutoField(verbose_name="Id de Publicacion", primary_key=True)
    id_usuario = models.CharField(max_length=20, blank=True, null=True)
    id_mascota = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_publicacion = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f"Publicacion {self.id_publicacion}"
    
    

class Mensaje(models.Model):
    id_mensaje = models.AutoField(verbose_name="Id de mensaje", primary_key=True)
    id_remitente = models.CharField(max_length=20, blank=True, null=True)
    id_destinatario = models.CharField(max_length=20, blank=True, null=True)
    id_publicacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_envio = models.DateField(verbose_name="Fecha de envio", blank=False, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Mensaje {self.id_mensaje}"