
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request): #MELO
    return HttpResponse("<h1>Welcome<h1>")

def saludo(request,username):
    return HttpResponse("<h1>Hola %s<h1>" % username)

def about(request): #MELO
    return HttpResponse("<h2>About</h2>")

def nosotros(request):
    return render(request,'paginas/nosotros.html')

#CODIGO HERLEY
def libros(request):
    return render(request,"libros/index.htm")

def libreria(request):
    return render(request,'templates/paginas/libros/index.html')