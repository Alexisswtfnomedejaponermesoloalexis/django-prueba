from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContactos
from django.shortcuts import get_object_or_404
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
# Create your views here.
def registros(request):

    alumnos=Alumnos.objects.all()

#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados
#
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

    return render(request,"registros/contacto.html")
#Indicamos el lugar donde se renderizará el resultado de esta vista

def comentarios(request):
    coments=ComentarioContactos.objects.all()
    return render(request, "registros/comentarios.html", {'comentarios':coments})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContactos, id=id)
    if request.method=='POST':
        comentarios.delete()
        comentarios=ComentarioContactos.objects.all()
        return render(request,"registros/consultaContacto.html",
                                        {'comentarios':comentarios})

    return render(request, confirmacion, {'object':comentario})

