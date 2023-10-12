
from django.http import HttpResponse

# Create your views here.
def index(request): #MELO
    return HttpResponse("<h1>Index page<h1>")

def saludo(request,username):
    return HttpResponse("<h1>Hola %s<h1>" % username)

def about(request): #MELO
    return HttpResponse("<h2>About</h2>")

#def nosotros(request):
#   return render(request,'paginas/nosotros.html')