## 4. Projeto da Solução

<span style="color:red">Pré-requisitos: <a href="03-Modelagem do Processo de Negocio.md"> Modelagem do Processo de Negocio</a></span>

## 4.1. Arquitetura da solução
Este projeto visa desenvolver uma plataforma digital chamada **RH Connect**, focada no apoio ao bem-estar e à saúde mental dos colaboradores de empresas por meio de um canal estruturado, seguro e funcional com o setor de Recursos Humanos. A solução busca modernizar os métodos tradicionais e ineficazes de comunicação entre colaboradores e RH, oferecendo um ambiente interativo, confidencial e baseado em dados para a escuta e o acompanhamento de situações sensíveis no cotidiano corporativo.

A arquitetura do sistema está estruturada em módulos bem definidos, utilizando **Python com Django** como framework base no backend. A comunicação entre as camadas é realizada por meio de APIs RESTful. O frontend poderá ser desenvolvido com **HTML/CSS/JavaScript**), e o banco de dados será gerenciado com **PostgreSQL**.

### 🔧 Tecnologias Utilizadas

| Camada         | Tecnologias                          |
|----------------|--------------------------------------|
| Backend        | Python 3.12, Django 5.x               |
| Frontend       | HTML5, CSS3, JavaScript (Bootstrap)   |
| Banco de Dados | PostgreSQL                           |
| Hospedagem     | Heroku ou Railway (fase inicial)     |

---

## 🧩 Módulos da Solução

### 1. Cadastro de Empresa
- Registro de novas empresas.
- Associação de usuário master à firma.

### 2. Cadastro de Usuário
- Registro de novos colaboradores e membros do RH.
- Associação dos usuários à firma (via e-mail institucional ou matrícula).
- Controle de perfis: colaborador, RH, gestor.

### 3. Criar Chamado Novo (Abertura)
- Interface intuitiva para abertura de chamados.
- Opção de anonimato e sigilo conforme escolha do colaborador.
- Encaminhamento automático para profissionais de RH.

### 4. Gestão dos Chamados
- Visualização e gerenciamento de chamados em andamento.
- Atribuição automática ou manual dos chamados ao RH.
- Atualização de status (aberto, em atendimento, encerrado).

### 5. Relatórios de Chamados
- Geração de relatórios por período, status e tipo de chamado.
- Indicadores de saúde mental e frequência de atendimento.
- Base para planejamento estratégico da organização.

### 6. Avaliar Chamado
- Formulário de avaliação pós-atendimento.
- Feedback anônimo opcional.

A seguir, são apresentados os protótipos desenvolvidos a partir dos processos identificados. Cada tabela representa um processo com os respectivos campos e características da interface.

### Processo 1: Cadastro de Empresa

| Atividade              | Protótipo (Figma/Imagem) | Nome do Campo     | Tipo de Campo | Observações                    |
|------------------------|--------------------------|-------------------|---------------|--------------------------------|
| Preencher formulário   | [Protótipo link/imagem]  | Nome da Empresa     | Texto         | Identificação da empresa             |
|                        |                          | Responsável administrativo     | Texto         | Identificação do responsável pelo RH Connect na empresa (usuário master)              |
|                        |                          | E-mail            | Texto         | Deve ser um e-mail corporativo.  |

---

### Processo 2: Cadastro de Colaborador

| Atividade              | Protótipo (Figma/Imagem) | Nome do Campo     | Tipo de Campo | Observações                    |
|------------------------|--------------------------|-------------------|---------------|--------------------------------|
| Preencher formulário   | [Protótipo link/imagem]  | Nome completo     | Texto         | Identificação              |
|                        |                          | E-mail            | Texto         | Deve ser um e-mail corporativo.  |
|                        |                          | Setor/departamento            | Texto         | Repartição na empresa onde o colaborador trabalha |
|                        |                          | Cargo            | Texto         | Função exercida |
|                        |                          | Tipo de usuário   | Dropdown      | RH, Colaborador, Gestor        |

---

### Processo 3: Criar Chamado Novo

| Atividade              | Protótipo                | Nome do Campo       | Tipo de Campo | Observações                        |
|------------------------|--------------------------|---------------------|---------------|------------------------------------|
| Preencher detalhes     | [Protótipo link/imagem]  | Título do chamado   | Texto         | Breve descrição do problema        |
|                        |                          | Descrição detalhada | Caixa de texto| Deve conter o relato completo      |
|                        |                          | Categoria            | Dropdown      | Assédio, Estresse, Outros          |
|                        |                          | Anexar arquivo       | Upload        | Opcional                           |
|                        |                          | Horário preferencial | Seletor       | Para facilitar o contato com o RH  |

---

### Processo 4: Gestão dos Chamados

| Atividade                | Protótipo                | Nome do Campo         | Tipo de Campo | Observações                       |
|--------------------------|--------------------------|------------------------|---------------|-----------------------------------|
| Visualizar chamados      | [Protótipo link/imagem]  | Lista de chamados      | Lista          | Exibe chamados com filtros        |
|                          |                          | Filtro por status      | Dropdown       | Em aberto, Em andamento, Finalizado |
|                          |                          | Filtro por colaborador | Campo texto    | Buscar por nome                   |
|                          |                          | Ações                  | Botões         | Visualizar / Finalizar / Avaliar  |

---

### Processo 5: Relatórios de Chamados

| Atividade                 | Protótipo                | Nome do Campo     | Tipo de Campo | Observações                        |
|---------------------------|--------------------------|-------------------|---------------|------------------------------------|
| Gerar relatório           | [Protótipo link/imagem]  | Período           | Calendário    | Seletor de datas                   |
|                           |                          | Categoria         | Dropdown      | Filtros por tipo de chamado        |
|                           |                          | Exportar          | Botão         | Exportar em PDF ou Excel           |

---

### Processo 6: Avaliar Chamado

| Atividade               | Protótipo                | Nome do Campo      | Tipo de Campo | Observações                        |
|-------------------------|--------------------------|--------------------|---------------|------------------------------------|
| Avaliar atendimento     | [Protótipo link/imagem]  | Nota               | Estrelas (1-5)| Avaliação do atendimento           |
|                         |                          | Comentários        | Caixa de texto| Feedback adicional (opcional)      |
|                         |                          | Enviar avaliação   | Botão         | Finaliza a avaliação               |

---

......  COLOQUE AQUI O SEU TEXTO E O DIAGRAMA DE ARQUITETURA .......

 Inclua um diagrama da solução e descreva os módulos e as tecnologias
 que fazem parte da solução. Discorra sobre o diagrama.
 
 **Exemplo do diagrama de Arquitetura**:
 
 ![Exemplo de Arquitetura](./images/arquitetura-exemplo.png)
 

### 4.2. Protótipos de telas

Visão geral da interação do usuário pelas telas do sistema e protótipo interativo das telas com as funcionalidades que fazem parte do sistema (wireframes).
Apresente as principais interfaces da plataforma. Discuta como ela foi elaborada de forma a atender os requisitos funcionais, não funcionais e histórias de usuário abordados nas <a href="02-Especificação do Projeto.md"> Especificação do Projeto</a>.
A partir das atividades de usuário identificadas na seção anterior, elabore o protótipo de tela de cada uma delas.
![Exemplo de Wireframe](images/wireframe-example.png)

São protótipos usados em design de interface para sugerir a estrutura de um site web e seu relacionamentos entre suas páginas. Um wireframe web é uma ilustração semelhante do layout de elementos fundamentais na interface.
 
> **Links Úteis**:
> - [Protótipos vs Wireframes](https://www.nngroup.com/videos/prototypes-vs-wireframes-ux-projects/)
> - [Ferramentas de Wireframes](https://rockcontent.com/blog/wireframes/)
> - [MarvelApp](https://marvelapp.com/developers/documentation/tutorials/)
> - [Figma](https://www.figma.com/)
> - [Adobe XD](https://www.adobe.com/br/products/xd.html#scroll)
> - [Axure](https://www.axure.com/edu) (Licença Educacional)
> - [InvisionApp](https://www.invisionapp.com/) (Licença Educacional)


## Diagrama de Classes

O diagrama de classes ilustra graficamente como será a estrutura do software, e como cada uma das classes da sua estrutura estarão interligadas. Essas classes servem de modelo para materializar os objetos que executarão na memória.

As referências abaixo irão auxiliá-lo na geração do artefato “Diagrama de Classes”.

> - [Diagramas de Classes - Documentação da IBM](https://www.ibm.com/docs/pt-br/rational-soft-arch/9.6.1?topic=diagrams-class)
> - [O que é um diagrama de classe UML? | Lucidchart](https://www.lucidchart.com/pages/pt/o-que-e-diagrama-de-classe-uml)

## Modelo ER

O Modelo ER representa através de um diagrama como as entidades (coisas, objetos) se relacionam entre si na aplicação interativa.]

As referências abaixo irão auxiliá-lo na geração do artefato “Modelo ER”.

> - [Como fazer um diagrama entidade relacionamento | Lucidchart](https://www.lucidchart.com/pages/pt/como-fazer-um-diagrama-entidade-relacionamento)


### 4.3. Modelo de dados

O desenvolvimento da solução proposta requer a existência de bases de dados que permitam efetuar os cadastros de dados e controles associados aos processos identificados, assim como recuperações.
Utilizando a notação do DER (Diagrama Entidade e Relacionamento), elaborem um modelo, na ferramenta visual indicada na disciplina, que contemple todas as entidades e atributos associados às atividades dos processos identificados. Deve ser gerado um único DER que suporte todos os processos escolhidos, visando, assim, uma base de dados integrada. O modelo deve contemplar, também, o controle de acesso de usuários (partes interessadas dos processos) de acordo com os papéis definidos nos modelos do processo de negócio.
_Apresente o modelo de dados por meio de um modelo relacional que contemple todos os conceitos e atributos apresentados na modelagem dos processos._

#### 4.3.1 Modelo ER

O Modelo ER representa através de um diagrama como as entidades (coisas, objetos) se relacionam entre si na aplicação interativa.]

As referências abaixo irão auxiliá-lo na geração do artefato “Modelo ER”.

> - [Como fazer um diagrama entidade relacionamento | Lucidchart](https://www.lucidchart.com/pages/pt/como-fazer-um-diagrama-entidade-relacionamento)

#### 4.3.2 Esquema Relacional

O Esquema Relacional corresponde à representação dos dados em tabelas juntamente com as restrições de integridade e chave primária.
 
As referências abaixo irão auxiliá-lo na geração do artefato “Esquema Relacional”.

> - [Criando um modelo relacional - Documentação da IBM](https://www.ibm.com/docs/pt-br/cognos-analytics/10.2.2?topic=designer-creating-relational-model)

![Exemplo de um modelo relacional](images/modeloRelacional.png "Exemplo de Modelo Relacional.")
---


#### 4.3.3 Modelo Físico

Insira aqui o script de criação das tabelas do banco de dados.

Veja um exemplo:

<code>

 -- Criação da tabela Médico
CREATE TABLE Medico (
    MedCodigo INTEGER PRIMARY KEY,
    MedNome VARCHAR(100)
);


-- Criação da tabela Paciente
CREATE TABLE Paciente (
    PacCodigo INTEGER PRIMARY KEY,
    PacNome VARCHAR(100)
);

-- Criação da tabela Consulta
CREATE TABLE Consulta (
    ConCodigo INTEGER PRIMARY KEY,
    MedCodigo INTEGER,
    PacCodigo INTEGER,
    Data DATE,
    FOREIGN KEY (MedCodigo) REFERENCES Medico(MedCodigo),
    FOREIGN KEY (PacCodigo) REFERENCES Paciente(PacCodigo)
);

-- Criação da tabela Medicamento
CREATE TABLE Medicamento (
    MdcCodigo INTEGER PRIMARY KEY,
    MdcNome VARCHAR(100)
);

-- Criação da tabela Prescricao
CREATE TABLE Prescricao (
    ConCodigo INTEGER,
    MdcCodigo INTEGER,
    Posologia VARCHAR(200),
    PRIMARY KEY (ConCodigo, MdcCodigo),
    FOREIGN KEY (ConCodigo) REFERENCES Consulta(ConCodigo),
    FOREIGN KEY (MdcCodigo) REFERENCES Medicamento(MdcCodigo)
);

</code>

Este script deverá ser incluído em um arquivo .sql na pasta src\bd.




### 4.4. Tecnologias

_Descreva qual(is) tecnologias você vai usar para resolver o seu problema, ou seja, implementar a sua solução. Liste todas as tecnologias envolvidas, linguagens a serem utilizadas, serviços web, frameworks, bibliotecas, IDEs de desenvolvimento, e ferramentas._

Apresente também uma figura explicando como as tecnologias estão relacionadas ou como uma interação do usuário com o sistema vai ser conduzida, por onde ela passa até retornar uma resposta ao usuário.


| **Dimensão**   | **Tecnologia**  |
| ---            | ---             |
| SGBD           | MySQL           |
| Front end      | HTML+CSS+JS     |
| Back end       | Java SpringBoot |
| Deploy         | Github Pages    |

