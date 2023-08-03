import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Usuario, Articulo, Comentario, Categoria, Contacto



# Create your views here.

def index(request):
    categorias = Categoria.objects.all()
    articulos_recientes = Articulo.objects.all().order_by('-fecha')[:3]
    articulos_mas_comentados = Articulo.objects.all().order_by('-comentario')[:3]
    return render(request, 'index.html', {'categorias': categorias, 'articulos_recientes': articulos_recientes, 'articulos_mas_comentados': articulos_mas_comentados})

def iniciar_sesion(request):
    error_message = None  

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('/')
        else:
            error_message = "Credenciales inválidas. Inténtalo de nuevo."

    return render(request, 'login.html', {'error_message': error_message})

def cerrar_sesion(request):
    logout(request)
    
    url_referencia = request.META.get('HTTP_REFERER')
    
    if not url_referencia:
        return redirect('/')
    
    return redirect('/')

def registrarse(request):
    if request.user.is_authenticated:
        url_referencia = request.META.get('HTTP_REFERER')
    
        if not url_referencia:
            return redirect('/')
        
        return redirect(url_referencia)
    
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']

        # Crear un nuevo usuario
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        Usuario.objects.create(user=user)

        # Iniciar sesión con el nuevo usuario
        login(request, user)

        return redirect('/')
    else:
        print("No se recibió una petición POST")

    return render(request, 'registrarse.html')

def categoria(request, id_categoria):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=id_categoria)
    articulos = Articulo.objects.filter(categoria=categoria)
    grupos = [articulos[i:i + 3] for i in range(0, len(articulos), 3)]
    return render(request, 'categorias.html', {'categoria': categoria, 'articulos': articulos, 'categorias': categorias, 'grupos': grupos})

def noticias(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.all()

    ordenar_por = request.GET.get('ordenar', 'titulo')
    ascendente = request.GET.get('asc-desc', 'asc')

    if ordenar_por == 'fecha':
        articulos = articulos.order_by('fecha' if ascendente == 'asc' else '-fecha')
    else:
        articulos = articulos.order_by('titulo' if ascendente == 'asc' else '-titulo')


    grupos = [articulos[i:i + 3] for i in range(0, len(articulos), 3)]
    return render(request, 'noticias.html', {'categorias': categorias, 'grupos': grupos})

@login_required
def crear_noticia(request):
    if not request.user.usuario.rol == 'C':
        return redirect('/')
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        fecha = datetime.datetime.now()
        imagen = request.FILES.get('imagen')
        categoria_id = request.POST.get('categoria')

        usuario = request.user.usuario

        # Crear el artículo y asignar el usuario como autor
        articulo = Articulo.objects.create(
            titulo=titulo,
            contenido=contenido,
            fecha=fecha,
            imagen=imagen,
            categoria_id=categoria_id,
            usuario=usuario
        )

        return redirect('/noticia/', id_noticia=articulo.id)
    
    categorias = Categoria.objects.all()
    return render(request, 'crear_noticia.html', {'categorias': categorias})

def noticia(request, id_noticia):
    articulo = get_object_or_404(Articulo, id=id_noticia)
    comentarios = Comentario.objects.filter(articulo=articulo)
    return render(request, 'noticia.html', {'articulo': articulo, 'comentarios': comentarios})

def acerca_de(request):
    return render(request, 'about.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        Contacto.objects.create(
            nombre=nombre,
            correo=correo,
            mensaje=mensaje
        )

        envio_exitoso = True

        return render(request, 'contact.html', {'envio_exitoso': envio_exitoso})
        
    return render(request, 'contact.html')

@login_required
def perfil(request):
    articulos = Articulo.objects.filter(usuario=request.user.usuario)
    comentarios = Comentario.objects.filter(usuario=request.user.usuario)
    return render(request, 'perfil.html', {'articulos': articulos, 'comentarios': comentarios})