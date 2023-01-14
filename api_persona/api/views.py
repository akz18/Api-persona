from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Persona,Tipo_persona
from api.serializers import PersonaSerializer,TipoPersonaSerializer

class TipoPersonaViewSet ( viewsets.ModelViewSet ):
    serializer_class = TipoPersonaSerializer
    queryset = Tipo_persona.objects.all()
   
class PersonaViewSet ( viewsets.ModelViewSet ):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

#... otras viewset
