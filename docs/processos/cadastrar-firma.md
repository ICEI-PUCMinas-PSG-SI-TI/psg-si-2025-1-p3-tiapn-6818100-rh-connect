### 3.3.2 Processo 2 – Login no RH Connect.

O processo se inicia quando colaborador entra no site do RH Connect, o mesmo ja possuirá uma conta, irá entrar e preencher seu login com o usuario e senha que serão previamente fornecidos.
Será realizado o preenchimento das informações, caso o usuario e senha estiverem corretos, o colaborador sera redirecionado ao site.

![image](https://github.com/user-attachments/assets/f1bfc905-5e54-479d-a3c3-826bea75db2e)



#### Detalhamento das atividades

**Login na plataforma**

| **Campo**       | **Tipo**         | **Restrições** | **Valor default** |
| ---             | ---              | ---            | ---               |
| [Nome do campo] | [tipo de dados]  |                |                   |
| ***Exemplo:***  |                  |                |                   |
| Login           | Caixa de Texto   | Formato de e-mail |                |
| Senha           | Caixa de Texto   | Mínimo de 12 caracteres |           |
| Botão Login           | Botão   | Usuario e senha corretos |           |

| **Comandos**         |  **Destino**                   | **Tipo** |
| ---                  | ---                            | ---               |
| [Nome do botão/link] | Atividade/processo de destino  | (default/cancel/  ) |
| ***Exemplo:***       |                                |                   |
| Entrar               | Fim do Processo              | default           |
