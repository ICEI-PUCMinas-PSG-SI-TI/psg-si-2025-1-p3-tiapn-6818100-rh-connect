# suporte/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chamados/abrir/', views.abrir_chamado, name='abrir_chamado'),
    # Adicione outras URLs aqui, como a de sucesso ou lista
    # Exemplo: path('chamados/sucesso/', views.pagina_sucesso, name='chamado_sucesso'),
    # Exemplo: path('', views.pagina_inicial, name='pagina_anterior_ou_home'),
]