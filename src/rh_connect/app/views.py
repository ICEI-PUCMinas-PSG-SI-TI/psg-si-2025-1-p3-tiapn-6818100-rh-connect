import datetime
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django import forms

from .forms import ChamadoForm
from .models import Chamado
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormMixin
from django.urls import reverse

class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        if self.request.user.cargo == self.request.user.CargoChoices.COMUM:
            return '/meus-chamados-comum/'
        if self.request.user.cargo == self.request.user.CargoChoices.RH:
            return '/todos-chamados/'


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
    

class TodosChamadosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Chamado
    template_name = "todos_chamados.html"
    context_object_name = "chamados"

    def test_func(self):
        return self.request.user.cargo == self.request.user.CargoChoices.RH

    def get_queryset(self):
        return Chamado.objects.all().order_by('-criado_em')
    

class ObservacaoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['observacao_rh', 'status']
        widgets = {
            'observacao_rh': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['observacao_rh'].required = False

class ChamadoDetailView(LoginRequiredMixin, UserPassesTestMixin, FormMixin, DetailView):
    model = Chamado
    template_name = "detalhe_chamado.html"
    context_object_name = "chamado"
    form_class = ObservacaoForm

    def test_func(self):
        return self.request.user.cargo == self.request.user.CargoChoices.RH

    def get_success_url(self):
        return reverse('detalhe_chamado', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()  # aqui é o ponto-chave!
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            form.save()
            return self.form_valid(form)
        return self.form_invalid(form)
    
from django.db.models.functions import TruncDate

def chamados_por_status(request):
    # Conta os chamados por status
    # Gráfico 1: chamados por status
    status_labels = ["ABERTO", "EM_ANALISE", "FECHADO"]
    chamados = Chamado.objects.values('status')
    contagem = {status: 0 for status in status_labels}
    for c in chamados:
        contagem[c['status']] += 1
    status_data = [contagem[status] for status in status_labels]
    status_cores = [
        'rgba(255, 99, 132, 0.7)',
        'rgba(54, 162, 235, 0.7)',
        'rgba(75, 192, 192, 0.7)'
    ]

    # Gráfico 2: chamados abertos por dia
    today = datetime.datetime.now().date()
    dias = [today - datetime.timedelta(days=i) for i in range(9, -1, -1)]
    dias_str = [d.strftime('%d/%m/%Y') for d in dias]
    dias_map = {d: 0 for d in dias}

    chamados_abertos = (
        Chamado.objects
        .filter(status='ABERTO', criado_em__date__gte=dias[0], criado_em__date__lte=dias[-1])
        .annotate(dia=TruncDate('criado_em'))
        .values('dia')
        .annotate(qtd=Count('id'))
    )
    for c in chamados_abertos:
        if c['dia'] in dias_map:
            dias_map[c['dia']] = c['qtd']

    dia_data = [dias_map[d] for d in dias]
    dia_cores = ['rgba(54, 162, 235, 0.7)' for _ in dias]

    context = {
        'status_labels': status_labels,
        'status_data': status_data,
        'status_cores': status_cores,
        'dia_labels': dias_str,
        'dia_data': dia_data,
        'dia_cores': dia_cores,
    }
    return render(request, 'chamados_grafico.html', context)
