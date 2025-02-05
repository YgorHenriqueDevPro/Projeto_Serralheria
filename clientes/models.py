from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=150)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
