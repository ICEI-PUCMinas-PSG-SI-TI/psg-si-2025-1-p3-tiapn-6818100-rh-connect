# suporte/urls.py

from django.urls import path
from .views import CriarChamadoView, CustomLoginView, MeusChamadosComumView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('meus-chamados-comum/', MeusChamadosComumView.as_view(), name='meus_chamados_comum'),
    path('criar-chamado/', CriarChamadoView.as_view(), name='criar_chamado'),
]