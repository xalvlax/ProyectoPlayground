from django.urls import path

from App_Coder.views import (
    CursoCreate, CursoDelete, CursoDetail, CursoList, CursoUpdate, buscar, busquedaCamada, crea_profesor, curso, 
    cursoFormulario, cursos, editar_profesor, eliminarProfesor, entregables, 
    estudiante, inicio, lista_curso, listaProfesores, loginView, profesores, register
    )

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_curso),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('entregables/', entregables, name="Entregables"),
    path('cursoFormulario/', cursoFormulario, name="CursoFormulario"),
    path('busquedaCamada/', busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar, name="Buscar"),
    path('listaProfesores/', listaProfesores, name="ListaProfesores"),
    path('crea-profesor/', crea_profesor, name="CreaProfesor"),
    path('elimina-profesor/<int:id>', eliminarProfesor, name="EliminarProfesor"),
    path('edita-profesor/<int:id>', editar_profesor, name="EditarProfesor"),
    path('listaCursos/', CursoList.as_view(), name="ListaCursos"),
    path('detalleCursos/<int:pk>', CursoDetail.as_view(), name="DetalleCursos"),
    path('creaCursos', CursoCreate.as_view(), name="CreaCursos"),
    path('actualizaCursos/<int:pk>', CursoUpdate.as_view(), name="ActualizaCursos"),
    path('eliminaCursos/<int:pk>', CursoDelete.as_view(), name="EliminaCursos"),
    path('login/', loginView, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
]
