
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    title = 'Django course!!'
    return render(request,'home.html',{
        'title'   : title
        })
#def project(request):
#    retunr(request)
  