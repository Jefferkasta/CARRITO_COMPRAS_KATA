from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('saludo/<str:username>',views.saludo),

    path('nosotros/',views.nosotros),
    path('libreria/',views.libreria),
    #path('libros/crear',views.crear, name='crear'),
    #path('libros/editar',views.editar, name='editar')
]