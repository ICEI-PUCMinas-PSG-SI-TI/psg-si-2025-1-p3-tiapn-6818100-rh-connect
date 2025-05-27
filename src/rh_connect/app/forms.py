# suporte/forms.py

from django import forms
from .models import Chamado, Colaborador

class ChamadoForm(forms.ModelForm):
    # Para permitir que o usuário selecione o colaborador.
    # Se você tiver um sistema de login e o chamador for sempre o usuário logado,
    # este campo pode ser preenchido automaticamente na view.
    colaborador = forms.ModelChoiceField(
        queryset=Colaborador.objects.all(), # Ou filtre conforme necessário
        label="Colaborador (Quem está abrindo o chamado)",
        widget=forms.Select(attrs={'class': 'form-control'}) # Adiciona uma classe para estilização
    )

    class Meta:
        model = Chamado
        fields = ['colaborador', 'titulo', 'descricao'] # Campos que aparecerão no formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Problema ao acessar o sistema XPTO'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Descreva detalhadamente o problema...'}),
        }
        labels = {
            'titulo': 'Título do Chamado',
            'descricao': 'Descrição Detalhada',
        }

    def __init__(self, *args, **kwargs):
        # Se você tiver um usuário logado e quiser preencher o colaborador automaticamente:
        # user = kwargs.pop('user', None) # Pega o usuário passado pela view
        super().__init__(*args, **kwargs)
        # if user and hasattr(user, 'colaborador_profile'): # Supondo que você tenha um perfil de colaborador ligado ao usuário
        #     self.fields['colaborador'].initial = user.colaborador_profile
        #     self.fields['colaborador'].widget = forms.HiddenInput() # Esconde o campo se preenchido automaticamente
        # elif user:
             # Se não houver perfil, mas você quiser restringir a seleção ou deixar em branco
             # self.fields['colaborador'].queryset = Colaborador.objects.filter(usuario_relacionado=user) # Exemplo
             # pass