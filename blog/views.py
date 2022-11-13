from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

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
    profesor.mail = mail
    profesor.save()
    messages.success(request, '¡Profesor editado!')
    return redirect('/ProfesorHome')