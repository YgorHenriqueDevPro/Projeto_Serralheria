from django.db import models

#Modelo para tabela cliente

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


#Modelo para tabela usuario

class Usuario(models.Model):       
    id_usuario = models.AutoField(primary_key=True)  # Definir id_usuario como chave primária
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    senha = models.CharField(max_length=100)    
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'usuario'  # Mantém o nome da tabela como 'usuario'