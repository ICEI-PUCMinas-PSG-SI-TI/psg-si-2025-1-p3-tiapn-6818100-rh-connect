## 3. Modelagem dos Processos de Negócio


> **Links Úteis**:
> - [Modelagem de Processos AS-IS x TO-BE](https://dheka.com.br/modelagem-as-is-to-be/)
> - [20 Dicas Práticas de Modelagem de Processos](https://dheka.com.br/20-dicas-praticas-de-modelagem-de-processos/)

### 3.1. Modelagem da situação atual (Modelagem AS IS)

Na contextualidade, sistemas de reclamação de RH possuem sistemas ineficientes e simplorios para a resolução de situações que afligem diretamente funcionarios de firmas, apenas realizando o envio de um formulario de reclamação, na esperança de uma melhoria posterior, mas nunca escutando a realidade do proximo, nosso sistema uma transformação na situação atual, disponibilizando o colaborador maneiras de contato mais efetivas e detalhadas para a resolução de problemas em seu dia a dia.

- Segue exemplo do processo utilizado na atualidade.
![image](https://github.com/user-attachments/assets/571d5a46-930e-4309-80d4-38eec54809a6)

### 3.2. Descrição geral da proposta (Modelagem TO BE)

O processo será entorno de uma ferramente de agendamento, inicialmente a firma será cadastrada na ferramente e vai informar quais são os colaboradores que são do setor de RH, após isso, os funcionarios do setor vão marcar horários de seu dia para disponibilizar seções para colaboradores que estão passam do algum tipo de situação, os interessados entraram na aplicação e poderão selecionar o melhor horario para conseguir comunicar-se com o time do RH.

### *Cadastro de Firmas na Plataforma*

Entrada: Preenchimento dos dados dos colaboradores e RH.

Saída: Sistema do RH Connect.

Onde acontece: RH Connect.

Participantes: Setor Administrativo, TI.

Produto de Informação: Disponibilização completa do sistema, desde a criação dos chamados, até o formulário de situação do colaborador.

### *Processamento de Chamados*

Entrada: Disponibilização de horário do RH para colaborador aderir e posteriormente criar o chamado.

Saída: Atendimento ao colaborador, relatórios sobre padrões de saúde mental.

Onde acontece: RH CONNECT.

Participantes: Psicólogo de RH (Lucas Mendes), colaboradores (como Carlos Silva).

Produto de Informação: Histórico de chamados, feedbacks sobre ações implementadas, formulário de resumo da situação do colaborador.

### *Planejamento Estratégico de Saúde Mental*

Entrada: Dados históricos, metas organizacionais.

Saída: Plano de ação para iniciativas de saúde mental.

Onde acontece: Reuniões de comitê gestor.

Participantes: Psicólogo de RH, alta liderança.

Produto de Informação: Plano estratégico, cronogramas e ações.

### *Gestão de Dados dos Chamados*

Entrada: Finalização do chamado

Saída: Historico de chamados e formulários

Onde acontece: RH Connect.

Processo Automatico, sem participantes.

### *Usuários do Sistema*
Psicólogo de RH (Lucas Mendes): Responsável por acessar e monitorar chamados, elaborar estratégias e intervenções.

Colaboradores (como Carlos Silva): Usuários do sistema para abertura de chamados e recebimento de suporte.

Equipe de TI: Gerencia o suporte técnico e a manutenção do sistema.

Gestores e Líderes de Equipe: Consultam relatórios e ajudam na tomada de decisões estratégicas.

### *Arquitetura do Software*
Banco de Dados:

Tabelas principais:

Usuários: Registro de dados dos colaboradores (apenas informações essenciais ou anonimizadas).

Chamados: Informações sobre chamados abertos, status, e resoluções.

Programas de Bem-Estar: Dados sobre palestras, workshops, e iniciativas.

Relatórios: Indicadores e análises de padrões.

- Segue exemplo da primeira proposta de resolução, a mesma sendo o conceito geral.
![image](https://github.com/user-attachments/assets/0cea4a50-77dd-4efd-9653-ba1b5400903b)

### 3.3. Modelagem dos processos

[PROCESSO 1 - Nome do Processo](./processos/processo-1-nome-do-processo.md "Detalhamento do Processo 1.")

[PROCESSO 2 - Nome do Processo](./processos/processo-2-nome-do-processo.md "Detalhamento do Processo 2.")
