from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    ROLES_CHOICES = (
        ('M', 'Miembro'),
        ('C', 'Colaborador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    rol = models.CharField(max_length=50, choices=ROLES_CHOICES, default='M', blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="usuarios")

    def __str__(self):
        return f"{self.user.username} - {self.rol}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="articulos")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre