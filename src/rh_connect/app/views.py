from django.shortcuts import render

# Create your views here.
# suporte/views.py

from django.shortcuts import render, redirect
from django.contrib import messages # Para exibir mensagens de feedback
# from django.contrib.auth.decorators import login_required # Se precisar que o usuário esteja logado
from .forms import ChamadoForm
from .models import Colaborador # Importe o Colaborador se for lidar com ele na view

# Busca
def loginpage(request):
    return render(request, 'loginpage.html')

# @login_required # Descomente se o usuário precisar estar logado
def abrir_chamado(request):
    if request.method == 'POST':
        # Para passar o usuário para o form, se necessário para preencher 'colaborador'
        # form = ChamadoForm(request.POST, user=request.user)
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False) # Não salva no banco ainda

            # Se o colaborador NÃO estiver no formulário e precisar ser definido pelo usuário logado:
            # Supondo que você tenha uma forma de ligar request.user a um Colaborador
            # try:
            #     colaborador_logado = Colaborador.objects.get(usuario=request.user) # Exemplo de relação
            #     chamado.colaborador = colaborador_logado
            # except Colaborador.DoesNotExist:
            #     messages.error(request, "Seu usuário não está vinculado a um colaborador.")
            #     return render(request, 'suporte/abrir_chamado.html', {'form': form})

            # O status_chamado e criado_em já têm defaults no model.
            chamado.save()
            messages.success(request, 'Chamado aberto com sucesso!')
            # Redireciona para uma página de sucesso ou para a lista de chamados
            return redirect('alguma_url_de_sucesso_ou_lista_chamados') # Crie essa URL
    else:
        # form = ChamadoForm(user=request.user) # Se precisar passar o usuário para inicializar o form
        form = ChamadoForm()

    context = {
        'form': form,
        'titulo_pagina': 'Abrir Novo Chamado'
    }
    
    return render(request, 'abrir_chamado.html', context)