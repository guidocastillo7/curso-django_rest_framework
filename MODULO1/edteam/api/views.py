from django.http import JsonResponse
from .models import Curso 
from django.views.decorators.csrf import csrf_exempt
import json

""" Usando Django puro, de manera clasica """

def index(request):
    context = {
        "status": True,
        "content": "mi primer api"
    }
    return JsonResponse(context)


def curso(request):
    listado_cursos = Curso.objects.all()
    context = {
        "status": True,
        "content": list(listado_cursos.values())
    }
    return JsonResponse(context)

@csrf_exempt
def post_curso(request):
    json_data = json.loads(request.body)

    titulo = json_data["titulo"]
    descripcion = json_data["descripcion"]
    imagen = json_data["imagen"]

    nuevo_curso = Curso.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        imagen=imagen
    )

    dic_nuevo_curso = {
        "id": nuevo_curso.id,
        "titulo": nuevo_curso.titulo,
        "descripcion": nuevo_curso.descripcion,
        "imagen": nuevo_curso.imagen
    }

    context = {
        "status": True,
        "content": dic_nuevo_curso
    }

    return JsonResponse(context)

""" Usando Django Rest Framework """
from rest_framework import generics
from rest_framework import serializers

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer