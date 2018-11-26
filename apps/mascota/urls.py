from django.conf.urls import url
from apps.mascota.views import MascotaList
from django.urls import path

urlpatterns = [
    path('listar/', MascotaList.as_view(), name='mascota_listar'),  
]    