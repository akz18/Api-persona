from rest_framework import serializers
from api.models import Persona, Tipo_persona

class TipoPersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tipo_persona
        fields = "__all__"

class PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"