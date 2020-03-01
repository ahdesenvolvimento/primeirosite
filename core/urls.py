from django1.urls import path

from core.views import index, clientes

urlpatterns = [
    path('', index, name='index'),
    path('cliente', clientes, name='clientes')
]