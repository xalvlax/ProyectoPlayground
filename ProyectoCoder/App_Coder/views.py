from django.http import HttpResponse
from django.shortcuts import render
from App_Coder.forms import CursoFormulario, ProfesorFormulario

from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from App_Coder.models import Curso, Profesor

# Create your views here.

def curso(self, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado</p>
    """)

def lista_curso(self):

    lista = Curso.objects.all()

    return render(self, "lista_cursos.html", {"lista_cursos": lista})


def inicio(self):

    return render(self, "inicio.html")

@staff_member_required(login_url='/app-coder/')
def estudiante(self):

    return render(self, "estudiantes.html")

def profesores(self):

    return render(self, "profesores.html")

def cursos(self):

    return render(self, "cursos.html")

def entregables(self):

    return render(self, "entregables.html")


# def cursoFormulario(request):

#     print('method:', request.method)
#     print('post:', request.POST)

#     if request.method == 'POST':

#         curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])

#         curso.save()

#         return render(request, 'inicio.html')

#     return render(request, "cursoFormulario.html")



def cursoFormulario(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            curso = Curso(nombre=data['curso'], camada=data['camada'])

            curso.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = CursoFormulario()

    return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})



def busquedaCamada(request):

    return render(request, 'busquedaCamada.html')


def buscar(request):
 

    if request.GET["camada"]:

        camada = request.GET["camada"]

        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "resultadoBusqueda.html", {"cursos": cursos, "camada": camada})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


@login_required
def listaProfesores(request):

    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}

    return render(request, "leerProfesores.html", contexto)


def crea_profesor(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])

            profesor.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = ProfesorFormulario()

    return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})



def eliminarProfesor(request, id):

    if request.method == 'POST':

        profesor = Profesor.objects.get(id=id)

        profesor.delete()

        profesores = Profesor.objects.all()

        contexto = {"profesores": profesores}

        return render(request, "leerProfesores.html", contexto)


def editar_profesor(request, id):

    print('method:', request.method)
    print('post:', request.POST)

    profesor = Profesor.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]

            profesor.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion,
        })

    return render(request, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})



class CursoList(LoginRequiredMixin, ListView):

    model = Curso
    template_name = 'curso_list.html'
    context_object_name = 'cursos'

class CursoDetail(DetailView):

    model = Curso
    template_name = 'curso_detail.html'
    context_object_name = 'curso'

class CursoCreate(CreateView):

    model = Curso
    template_name = 'curso_create.html'
    fields = ["nombre", "camada"]
    success_url = '/app-coder/'

class CursoUpdate(UpdateView):

    model = Curso
    template_name = 'curso_update.html'
    fields = ('__all__')
    success_url = '/app-coder/'

class CursoDelete(DeleteView):

    model = Curso
    template_name = 'curso_delete.html'
    success_url = '/app-coder/'



def loginView(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})

            else:

                return render(request, "inicio.html", {"mensaje": "Error, datos incorrectos"})

        return render(request, "inicio.html", {"mensaje": "Error, formulario invalido"})

    else:

        miFormulario = AuthenticationForm()

    return render(request, "login.html", {"miFormulario": miFormulario})


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado'})

    else:

        form = UserCreationForm()

    return render(request, "registro.html", {"miFormulario": form})


