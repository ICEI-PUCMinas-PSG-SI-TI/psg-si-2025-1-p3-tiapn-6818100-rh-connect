### 3.3.3 Processo 4 – Finalizar chamado.
 
O processo depende do chamado *2 - Abertura de chamado*, caso existir algum chamado em aberto.
Caso exista o chamado, o funcionario do RH podera acessar o chamado, preencher as observações do mesmo e clicar em um botão para fechar o chamado.
Caso se as observações não forem preenchidas, o chamado não será fechado.

![image](https://github.com/user-attachments/assets/b0b93ec5-73ab-40b5-b33b-4f38c5c334c7)

#### Detalhamento das atividades

**Fechamento de chamado**

| **Campo**       | **Tipo**         | **Restrições** | **Valor default** |
| ---             | ---              | ---            | ---               |
| [Nome do campo] | [tipo de dados]  |                |                   |
| ***Exemplo:***  |                  |                |                   |
| Observações          | Área de texto   | obrigatorio o preenchimento |                |
| Fechar chamado          | Seleção única   | observação deve estar preenchida |           |

| **Comandos**         |  **Destino**                   | **Tipo** |
| ---                  | ---                            | ---               |
| [Nome do botão/link] | Atividade/processo de destino  | (default/cancel/  ) |
| ***Exemplo:***       |                                |                   |
| fechar chamado               |Fim do processo        | default           |
