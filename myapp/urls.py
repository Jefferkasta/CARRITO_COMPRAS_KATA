from django.urls import path
from . import views

urlpatterns = [
    path('',views.saludo),
    path('about/',views.about)
]