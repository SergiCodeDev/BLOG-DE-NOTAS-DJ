from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar, name='agregar'),
    path('eliminar/<int:nota_id>/', views.eliminar, name='eliminar'),
    path('editar/<int:nota_id>/', views.editar, name='editar'),
]