from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from CdH import views

urlpatterns = [
    #URL's para Recepcionistas
    path('index/', views.index),
    path('servicios/', views.services, name="servicios"),
    path('referencias/', views.references, name="referencias"),
    path('ver_noticia/<int:id>', views.ver_noticia, name="ver_noticia"),
    path('editar_noticia/<int:id>', views.editar_noticia, name="editar_noticia"),
    path('actualizar_noticia/<int:id>', views.actualizar_noticia, name="actualizar_noticia"),
    path('crear_noticia', views.crear_noticia, name="crear_noticia"),
    path('guardar_noticia', views.guardar_noticia, name="guardar_noticia"),
]