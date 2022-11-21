from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.utils import timezone

# Create your views here.

@login_required

def home(request):
    cursoslistado = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursoslistado})

def NuevoCurso(request):
    codigo = request.POST['CodigoTxt']
    nombre = request.POST['NombreTxt']
    créditos = request.POST['CreditosNum']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=créditos)
    messages.success(request, '¡Curso nuevo creado!')
    return redirect('/')

def EliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso eliminado!')
    return redirect('/')

def EditarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "EditarCurso.html", {"curso": curso})

def EditCurso(request):
    codigo = request.POST['CodigoTxt']
    nombre = request.POST['NombreTxt']
    créditos = request.POST['CreditosNum']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = créditos
    curso.save()
    messages.success(request, '¡Curso editado!')
    return redirect('/')

@login_required
def EstudiantesHome(request):
    estudianteslistado = Estudiante.objects.all()
    return render(request, "estudiante.html", {"estudiantes": estudianteslistado})

def NuevoEstudiante(request):
    documento = request.POST['DocumentoTxt']
    nombre = request.POST['NombreTxt']
    apellido = request.POST['ApellidoTxt']
    mail = request.POST['EmailTxt']

    estudiante = Estudiante.objects.create(documento=documento, nombre=nombre, apellido=apellido, email=mail)
    messages.success(request, '¡Nuevo estudiante creado!')
    return redirect('/EstudianteHome')

def EliminarEstudiante(request, documento):
    estudiante = Estudiante.objects.get(documento=documento)
    estudiante.delete()
    messages.success(request, '¡Estudiante eliminado!')
    return redirect('/EstudianteHome')

def EditarEstudiante(request, documento):
    estudiante = Estudiante.objects.get(documento=documento)
    return render(request, "EditarEstudiante.html", {"estudiante": estudiante})

def EditEstudiante(request):
    documento = request.POST['DocumentoTxt']
    nombre = request.POST['NombreTxt']
    apellido = request.POST['ApellidoTxt']
    mail = request.POST['EmailTxt']

    estudiante = Estudiante.objects.get(documento=documento)
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.mail = mail
    estudiante.save()
    messages.success(request, '¡Estudiante editado!')
    return redirect('/EstudianteHome')

@login_required
def ProfesorHome(request):
    profesorlistado = Profesor.objects.all()
    return render(request, "profesor.html", {"profesores": profesorlistado})

def NuevoProfesor(request):
    id = request.POST['IDNum']
    nombre = request.POST['NombreTxt']
    apellido = request.POST['ApellidoTxt']
    mail = request.POST['EmailTxt']
    profesion = request.POST['ProfesionTxt']

    profesor = Profesor.objects.create(id=id, nombre=nombre, apellido=apellido, email=mail, profesion=profesion)
    messages.success(request, '¡Nuevo profesor creado!')
    return redirect('/ProfesorHome')

def EliminarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    messages.success(request, '¡Profesor eliminado!')
    return redirect('/ProfesorHome')

def EditarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    return render(request, "EditarProfesor.html", {"profesor": profesor})

def EditProfesor(request):
    id = request.POST['IDNum']
    nombre = request.POST['NombreTxt']
    apellido = request.POST['ApellidoTxt']
    mail = request.POST['EmailTxt']
    profesion = request.POST['ProfesionTxt']

    profesor = Profesor.objects.get(id=id)
    profesor.nombre = nombre
    profesor.apellido = apellido
    profesor.email = mail
    profesor.profesion = profesion
    profesor.save()
    messages.success(request, '¡Profesor editado!')
    return redirect('/ProfesorHome')

def salir (request):
    logout(request)
    return redirect('/')

@login_required
def ArticuloHome(request):
    articulolistado = Articulos.objects.all()
    return render(request, "blog.html", {"articulos": articulolistado})

def NuevoArticulo(request):
    titulo = request.POST['TituloTxt']
    contenido = request.POST['ContenidoTxt']
    imagen = request.POST['ImgUrl']
    autor = request.POST['AutorTxt']

    articulo = Articulos.objects.create(titulo=titulo, contenido=contenido, imagen=imagen, autor=autor)
    messages.success(request, '¡Nuevo artículo creado!')
    return redirect('/ArticuloHome')

def EliminarArticulo(request, titulo):
    articulo = Articulos.objects.get(titulo=titulo)
    articulo.delete()
    messages.success(request, '¡Artículo Eliminado!')
    return redirect('/ArticuloHome')

def EditarArticulo(request, titulo):
    articulo = Articulos.objects.get(titulo=titulo)
    return render(request, "EditarBlog.html", {"articulo": articulo})

def EditArticulo(request):
    titulo = request.POST['TituloTxt']
    contenido = request.POST['ContenidoTxt']
    imagen = request.POST['ImgUrl']
    autor = request.POST['AutorTxt']

    articulo = Articulos.objects.get(titulo=titulo)
    articulo.titulo = titulo
    articulo.contenido = contenido
    articulo.imagen = imagen
    articulo.autor = autor
    articulo.save()
    messages.success(request, '¡Articulo editado!')
    return redirect('/ArticuloHome')

def LeerArticulo(request, titulo):
    articulo = Articulos.objects.get(titulo=titulo)
    return render(request, "LeerArticulo.html", {"articulo": articulo})