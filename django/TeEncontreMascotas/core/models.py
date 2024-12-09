from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(verbose_name="Id de Usuario", primary_key=True)
    rut = models.CharField(max_length=12, null=False, default="none")
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    contrasenia = models.CharField(verbose_name="Contraseña",max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    fono = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

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
    imagen = models.ImageField(null=True, default="null", blank=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Mascota {self.nombre}"

class Favoritos(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_mascota = models.ManyToManyField(Mascota)

class Publicacion(models.Model):
    id_publicacion = models.AutoField(verbose_name="Id de Publicacion", primary_key=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_publicacion = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f"Publicacion {self.id_publicacion}"
    
    

class Mensaje(models.Model):
    id_mensaje = models.AutoField(verbose_name="Id mensaje", primary_key=True)
    id_remitente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)    
    contenido = models.CharField(max_length=500, default="")
    fecha_envio = models.DateField(verbose_name="Fecha de envio", blank=False, null=False)

    def __str__(self):
        return f"Mensaje {self.id_mensaje}"