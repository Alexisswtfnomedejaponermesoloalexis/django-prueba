from django.shortcuts import render
from .models import Alumnos
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
# Create your views here.
def registros(request):

    alumnos=Alumnos.objects.all()

#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados