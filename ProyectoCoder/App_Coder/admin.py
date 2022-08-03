from django.contrib import admin

from .models import Curso, Entregable, Estudiante, Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'profesion', 'email']
    search_fields = ['nombre', 'apellido']

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable)
