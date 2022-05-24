from django import views
from django.urls import path # funcion para esta ruta tal view, confguracion de ursl
from . import views

urlpatterns =[

    path("cursos" , views.cursos),
    path("alta_curso/<nombre>" , views.alta_curso)

]
