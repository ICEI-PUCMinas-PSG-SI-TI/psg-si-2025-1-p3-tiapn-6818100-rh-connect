# suporte/urls.py

from django.urls import path
from .views import ChamadoDetailView, CriarChamadoView, CustomLoginView, MeusChamadosComumView, TodosChamadosView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('meus-chamados-comum/', MeusChamadosComumView.as_view(), name='meus_chamados_comum'),
    path('criar-chamado/', CriarChamadoView.as_view(), name='criar_chamado'),
    path('todos-chamados/', TodosChamadosView.as_view(), name='todos_chamados'),
    path('chamados/<int:pk>/', ChamadoDetailView.as_view(), name='detalhe_chamado'),
]