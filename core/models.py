from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF', primary_key=True)
    profissao = models.CharField('Profissão', max_length=50)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF', primary_key=True)
    cargo = models.CharField('Cargo', max_length=50)
    funcao = models.CharField('Função', max_length=50)

    def __str__(self):
        return self.nome


class Dono(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF', primary_key=True)
