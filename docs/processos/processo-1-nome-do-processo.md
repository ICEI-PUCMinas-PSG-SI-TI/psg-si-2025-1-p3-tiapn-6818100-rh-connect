3.3.1 – Processo 1: Cadastro de chamado e Processamento
Descrição do Processo:
Este processo é responsável por permitir que o colaborador realize o cadastro de um chamado por meio da plataforma RH Connect. A partir disso, o sistema processa o agendamento com o setor de RH, disponibiliza os horários e confirma o atendimento.

Modelo BPMN:


Detalhamento das Atividades:
✅ Nome da Atividade 1: Preencher Formulário de Chamado
Campo	Tipo de Dados	Restrições	Valor Default
nome	Caixa de Texto	obrigatório	
email	Caixa de Texto	formato de e-mail	
descrição do problema	Área de Texto	mínimo de 30 caracteres	
tipo de situação	Seleção Única	opções: Assédio, Carga Excessiva, Ambiente Tóxico, Outro	
documento anexo	Arquivo	opcional	
Comandos

Nome do Botão	Destino	Tipo
cadastrar chamado	Atividade 2 (Escolher horário)	default
cancelar	Fim do processo	cancel
✅ Nome da Atividade 2: Escolher Horário com RH
Campo	Tipo de Dados	Restrições	Valor Default
data preferida	Data	não pode ser anterior à data atual	
horário preferido	Hora	dentro do horário comercial (08h–18h)	
modo de atendimento	Seleção Única	opções: Presencial, Online	
Comandos

Nome do Botão	Destino	Tipo
confirmar horário	Atividade 3 (Confirmação do chamado)	default
voltar	Atividade 1 (Formulário)	cancel
✅ Nome da Atividade 3: Confirmação do Chamado
Campo	Tipo de Dados	Restrições	Valor Default
status do chamado	Caixa de Texto	somente leitura	Aguardando atendimento
resumo do agendamento	Área de Texto	somente leitura	
link da reunião	Link	somente se for online	
Comandos

Nome do Botão	Destino	Tipo
finalizar cadastro	Fim do processo	default
editar informações	Atividade 1	cancel
