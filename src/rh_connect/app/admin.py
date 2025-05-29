from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empresa, Colaborador, Chamado


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cnpj", "nome_responsavel", "email_responsavel")
    search_fields = ("nome", "cnpj", "nome_responsavel")


@admin.register(Colaborador)
class ColaboradorAdmin(UserAdmin):
    model = Colaborador
    list_display = ("username", "first_name", "last_name", "email", "empresa", "cargo", "departamento", "is_staff")
    list_filter = ("empresa", "cargo", "departamento", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Dados Corporativos", {
            "fields": ("empresa", "cargo", "departamento", "status")
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Dados Corporativos", {
            "fields": ("empresa", "cargo", "departamento", "status")
        }),
    )
    search_fields = ("username", "email", "first_name", "last_name")


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "colaborador", "criado_em")
    search_fields = ("titulo", "descricao", "colaborador__username")
    list_filter = ("criado_em",)
    date_hierarchy = "criado_em"
