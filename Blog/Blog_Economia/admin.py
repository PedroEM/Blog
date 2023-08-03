from django.contrib import admin
from .models import Usuario, Categoria, Articulo, Comentario, Contacto

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Comentario)
admin.site.register(Contacto)