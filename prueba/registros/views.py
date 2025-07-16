from urllib import request
from django.shortcuts import redirect, render
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos 
from .forms import FormArchivos
from django.contrib import messages



# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})
#Indicamos el lugar donde se renderizará el resultado deesta vista

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            
            return redirect('Comentarios')        
    form = ComentarioContactoForm()
#Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})


def contacto(request):
    form = ComentarioContactoForm()
    return render(request,"registros/contacto.html", {'form': form})
#Indicamos el lugar donde se renderizará el resultado de esta vista


def comentarios(request):
    coments=ComentarioContacto.objects.all()
    return render(request, "registros/comentario.html", {'comentarios':coments})

def eliminarComentarioContacto(request, id,
    confirmacion= 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/comentario.html",
                      {'comentarios':comentarios})
    return render(request, confirmacion, {'object': comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)

    return render(request, "registros/formEditarComentario.html", 
        {'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)

    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/comentario.html",
        {'comentarios': comentarios})
    

    return render(request, "registros/formEditarComentario.html", 
    {'comentario': comentario})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivos']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else: 
            messages.error(request, "Error al procesar el formulario")

    else: 
     return render(request, "registros/archivos.html", {'archivo': Archivos})
    
    
####################################################################################################################3

#16/07/2025 CONSULTAS DIRECTAS CON SQL 

def consultasSQL(request):

    alumnos = Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request,"registros/consultas.html", {'alumnos':alumnos})