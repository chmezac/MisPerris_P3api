from django.conf.urls import url
from apps.mascota.views import *
from django.urls import path

urlpatterns = [
    path('listar/', MascotaList.as_view(), name='mascota_listar'),  
]    