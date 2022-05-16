from django.shortcuts import redirect, render
from django.http import HttpResponse

from CdH.models import Noticia


def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'servicios.html')

def references(request):
    return render (request, 'referencias.html')

def ver_noticia(request):
    return render (request, 'ver_noticia.html')

def editar_noticia(request, id):
    return render (request, 'editar_noticia.html')

def crear_noticia(request):
    return render (request, 'crear_noticia.html')

def guardar_noticia(request):
    post=Noticia()
    post.titulo=request.POST.get('titulo')
    post.cuerpo=request.POST.get('cuerpo')
    post.resumen=request.POST.get('resumen')
    post.fecha=request.POST.get('fecha')
    post.imagen=request.POST.get('imagen')
    post.save()

    return redirect ('ver_noticia')

def actualizar_noticia(request, id):
    usuario=Noticia.objects.all()
    post=next(post for post in usuario if post.pk==id)
    post.nombre=request.POST.get('nombre')
    post.nombreu=request.POST.get('nombreu')
    post.tipo=request.POST.get('tipo')
    post.correo=request.POST.get('mail')
    post.apellidos=request.POST.get('apellidos')
    post.contraseña=request.POST.get('contraseña')
    post.save()
    
