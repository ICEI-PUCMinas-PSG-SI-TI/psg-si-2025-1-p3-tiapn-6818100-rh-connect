from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    nome_responsavel = models.CharField(max_length=255)
    email_responsavel = models.EmailField()

    def __str__(self):
        return self.nome


class Colaborador(AbstractUser):
    class CargoChoices(models.TextChoices):
        COMUM = "COMUM", "Comum"
        RH = "RH", "RH"

    class DepartamentoChoices(models.TextChoices):
        FINANCEIRO = "FINANCEIRO", "Financeiro"
        ADMINISTRATIVO = "ADMINISTRATIVO", "Administrativo"
        TECNOLOGIA = "TECNOLOGIA", "Tecnologia"
        RH = "RH", "Recursos Humanos"
        OUTRO = "OUTRO", "Outro"

    departamento = models.CharField(
        max_length=20,
        choices=DepartamentoChoices.choices,
        default=DepartamentoChoices.OUTRO
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='colaboradores', null=True, blank=True)
    cargo = models.CharField(
        max_length=10,
        choices=CargoChoices.choices,
        default=CargoChoices.COMUM
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Chamado(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='chamados')
    observacao_rh = models.TextField()

    def __str__(self):
        return f"{self.titulo} - {self.colaborador.username}"

