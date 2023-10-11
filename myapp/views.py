
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("<h1>Hello, world!<h1>")

def about(request):
    return HttpResponse('<h1>About<h1>')