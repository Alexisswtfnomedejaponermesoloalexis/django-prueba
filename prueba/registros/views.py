from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContactos
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages
from .models import Archivos
from .forms import FormArchivos
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
    comentarios=ComentarioContactos.objects.all()
    return render(request, "registros/comentarios.html", {'comentarios':comentarios})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContactos, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContactos.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})

    return render(request, confirmacion, {'object':comentario})



def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:

            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})








#####################################################################################################3

def consultar1(request):
    #con una sola consulta
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar2(request):
    #con dos consultas
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar3(request):
    #Si solo deseamos recuperar ciertos datos agregamos la funcion #only, listando
    #los campos que queremos obtener de la consulta a emplear filter() o en el ejemplo all()
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

#EXPRESIONES 

# __contains : LIKE
# __exact :  IGUAL
# __iexact :  NO DISTINGUE ENTRE MAYUSCULAS Y MINUSCULAS
# __lt : MENOR QUE
# __lte _ MENOR O IGUAL QUE
# __gt: MAYOR QUE
# __gte : MAYOR O IGUAL QUE
# __in : LOS QUE COINCIDAN CON LOS PARAMETROS ASIGNADOS

{}
def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2025, 6, 20)
    fechaFin=datetime.date(2025, 7, 20)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='buen alumno')
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


#####################################################################################
# P R A C T I C A 10/07/2025


#CONSULTA 1
def consultar8(request):
    fecha_inicio = datetime.date(2025, 6, 8)
    fecha_fin = datetime.date(2025, 7, 10)
    comentarios = ComentarioContactos.objects.filter(created__range=(fecha_inicio, fecha_fin))
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})
#CONSULTA 2
def consultar9(request):
    comentarios = ComentarioContactos.objects.filter(mensaje__contains="hola")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

#CONSULTA 3
def consultar10(request):
    comentarios = ComentarioContactos.objects.filter(usuario__exact="Juan")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

#CONSULTA 4
def consultar11(request):
    lista_mensajes = ComentarioContactos.objects.values_list('mensaje')
    for mensaje in lista_mensajes:
        print(mensaje)
    return redirect('Comentario')

#CONSULTA 5
def consultar12(request):
    comentarios = ComentarioContactos.objects.filter(mensaje__startswith="Bu")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})