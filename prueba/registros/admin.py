from django.contrib import admin
from registros.models import Alumnos
from registros.models import Comentario
from .models import ComentarioContacto


# Register your models here.

class AdministarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula','nombre', 'carrera', 'turno','created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno') 
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ('created','updated', 'matricula', 'carrera', 'turno')
        else:
            return('created', 'updated')

admin.site.register(Alumnos, AdministarModelo)

class AdministarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)