from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ChamadoForm
from .models import Chamado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        if self.request.user.cargo == self.request.user.CargoChoices.COMUM:
            return '/meus-chamados-comum/'
        if self.request.user.cargo == self.request.user.CargoChoices.RH:
            return '/meus-chamados-rh/'


@method_decorator(login_required, name='dispatch')
class MeusChamadosComumView(ListView):
    model = Chamado
    template_name = "meus_chamados_comum.html"
    context_object_name = "chamados"

    def get_queryset(self):
        return Chamado.objects.filter(colaborador=self.request.user).order_by('-criado_em')

class CriarChamadoView(LoginRequiredMixin, CreateView):
    model = Chamado
    form_class = ChamadoForm
    template_name = 'criar_chamado.html'
    success_url = reverse_lazy('meus_chamados_comum')

    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)