from rest_framework import generics
from .models import Mascota
from .serializers import MascotaSerializer
from django.shortcuts import get_object_or_404

class MascotaList(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    
    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

    