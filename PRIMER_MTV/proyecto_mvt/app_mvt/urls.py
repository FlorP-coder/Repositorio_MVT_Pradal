from django.urls import path
from . import views

urlpatterns = [
    path ("familia/", views.familia),
    path ("ingreso_flia/<nombre>/<edad>/<relacion>/<fecha_nac>", views.ingreso_flia),
]