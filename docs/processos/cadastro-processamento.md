### 3.3.1 Processo 2 – Cadastro de chamado e Processamento.

_O processo se inicia com o colaborador abrindo o chamado para o RH, que irá conferir se o horário será efetivo para a realização do chamado._
_Caso se o processo for positivo, o funcionário do setor de RH vai aceitar o chamado, fazendo que o sistema dispare uma confirmação para o colaborador._
_Após o recebimento da confirmação, os colaboradores irão realizar uma reunião em particular, conversando sobre a(s) situação(ões) do requisitadas pelo adjunto._
_Ao termino da reunião, o chamado será fechado, finalizando o processo._

![image](https://github.com/user-attachments/assets/6e3a50e9-4243-4a9d-b132-745ee80da7c5)

#### Detalhamento das atividades

**Abertura de Chamado (Colaborador)**

| **Campo**       | **Tipo**         | **Restrições** | **Valor default** |
| ---             | ---              | ---            | ---               |
| [Nome do campo] | [tipo de dados]  |                |                   |
| nome do chamado | Caixa de Texto   | preenchimento obrigatorio |                   |
| descrição do chamado | Área de Texto   |          |           |

| **Comandos**         |  **Destino**                   | **Tipo** |
| ---                  | ---                            | ---               |
| [Nome do botão/link] | Atividade/processo de destino  | (default/cancel/  ) |
| ***Exemplo:***       |                                |                   |
| postar chamado   | Fim do Processo              | default           |
| redirecionamento | Envio de informações para RH |                   |


**Painel de Chamados (RH)**

| **Campo**       | **Tipo**         | **Restrições** | **Valor default** |
| ---             | ---              | ---            | ---               |
| [Nome do campo] | [tipo de dados]  |                |                   |
| chamado | Caixa de Texto |                |                   |

| **Comandos**         |  **Destino**                   | **Tipo**          |
| ---                  | ---                            | ---               |
| [Nome do botão/link] | Atividade/processo de destino  | (default/cancel/  ) |
| abrir chamado | Fim do Processo | default |
| redirecionamento | Abertura da pagina do chamado selecionado |      |

**Aceitar Chamado (RH)**

| **Campo**       | **Tipo**         | **Restrições** | **Valor default** |
| ---             | ---              | ---            | ---               |
| [Nome do campo] | [tipo de dados]  |                |                   |
| checkbox aceitar chamado | Seleção única |                |                   |
| checkbox voltar pagina | Seleção única |      |


| **Comandos**         |  **Destino**                   | **Tipo**          |
| ---                  | ---                            | ---               |
| [Nome do botão/link] | Atividade/processo de destino  | (default/cancel/  ) |
| aceitar chamado | muda estado do chamado para aceito e finaliza o processo | default |
| voltar pagina | volta para pagina de Painel de Chamados | cancel |
