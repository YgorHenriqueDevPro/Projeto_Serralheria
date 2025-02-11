from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)  # Definir id_cliente como chave primária
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=150)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'cliente'  # Mantém o nome da tabela como 'cliente'
