from .models import Mascota
from rest_framework import serializers

class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ('nombre', 'raza', 'descripcion', 'state')

