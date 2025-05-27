# Create your models here.
from django.db import models
from django.utils import timezone # Para o campo Criado_em

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True) 
    nome_responsavel = models.CharField(max_length=255)
    email_responsavel = models.EmailField()
    status = models.CharField(max_length=100) 

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

class Colaborador(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='colaboradores')
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True) 
    departamento = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

class Chamado(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True, blank=True, related_name='chamados')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now) 

    STATUS_CHOICES = [
        ('ABERTO', 'Aberto'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('AGUARDANDO_CLIENTE', 'Aguardando Cliente'),
        ('RESOLVIDO', 'Resolvido'),
        ('FECHADO', 'Fechado'),
    ]
    status_chamado = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ABERTO',
    )


    def __str__(self):
        return f"{self.titulo} (Colaborador: {self.colaborador.nome if self.colaborador else 'N/A'})"

    class Meta:
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"
        ordering = ['-criado_em'] 