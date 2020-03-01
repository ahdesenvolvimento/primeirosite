from django.contrib import admin

from .models import Cliente, Funcionario, Dono
# Register your models here
admin.site.register(Cliente)
admin.site.register(Dono)
admin.site.register(Funcionario)