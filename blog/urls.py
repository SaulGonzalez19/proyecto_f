from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('NuevoCurso/', views.NuevoCurso),
    path('EliminarCurso/<codigo>', views.EliminarCurso),
    path('EditarCurso/<codigo>', views.EditarCurso),
    path('EditCurso/', views.EditCurso),
    path('EstudianteHome/', views.EstudiantesHome),
    path('EstudianteHome/NuevoEstudiante/', views.NuevoEstudiante),
    path('EstudianteHome/EliminarEstudiante/<documento>', views.EliminarEstudiante),
    path('EstudianteHome/EditarEstudiante/<documento>', views.EditarEstudiante),
    path('EstudianteHome/EditEstudiante/', views.EditEstudiante),
    path('ProfesorHome/', views.ProfesorHome),
    path('ProfesorHome/NuevoProfesor/', views.NuevoProfesor),
    path('ProfesorHome/EliminarProfesor/<id>', views.EliminarProfesor),
    path('ProfesorHome/EditarProfesor/<id>', views.EditarProfesor),
    path('ProfesorHome/EditProfesor/', views.EditProfesor),
]