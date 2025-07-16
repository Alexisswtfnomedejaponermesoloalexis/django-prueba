from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

def principal(request):
    return render(request, 'inicio/principal.html')

menu="""
<a href="/">Home</a>
<a href="/formulario/">Formulario</a>
<a href="/contacto/">Contacto</a>
"""

def contacto(request):
    contenido = """<h2>Contacto</h2>
    <p>Nombre:<input type="text" name="nombre"></p>
    <p>Mensaje:<textarea col="50" rows="10"></textarea></p>
    <p><input type="Button" name="enviar" value="Enviar"></p>"""
    return render(request, 'inicio/contacto.html', {'contenido': contenido, 'menu': menu})


def formulario(request):
    contenido = """<h2>Registrar </h2>
    <p>Matricula:<input type="text" name="matricula"></p>
    <p>Nombre:<input type="text" name="nombre"></p>
    <p>Carrera:
    <select name="carrera">
        <option>ING. DGS</option>
        <option>ING. EVND</option>
    <select>
    </p>
    <input type="radio" name"turno" value="matutino">Matutino
    <input type="radio" name"turno" value="vespertino">Vespertino
    <p><input type="Button" name="enviar" value="Enviar"></p>
    """
    return render(request, 'inicio/formulario.html', {'contenido': contenido})


def ejemplo(request):
    return render(request, 'inicio/ejemplo.html')

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST) # type: ignore
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            
            return redirect('Comentarios')        
    form = ComentarioContactoForm() # type: ignore
#Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form':form})

        