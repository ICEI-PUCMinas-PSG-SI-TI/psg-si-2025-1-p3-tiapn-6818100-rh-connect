## 4. Projeto da Solução

<span style="color:red">Pré-requisitos: <a href="03-Modelagem do Processo de Negocio.md"> Modelagem do Processo de Negocio</a></span>

## 4.1. Arquitetura da solução
Este projeto visa desenvolver uma plataforma digital chamada **RH Connect**, focada no apoio ao bem-estar e à saúde mental dos colaboradores de empresas por meio de um canal estruturado, seguro e funcional com o setor de Recursos Humanos. A solução busca modernizar os métodos tradicionais e ineficazes de comunicação entre colaboradores e RH, oferecendo um ambiente interativo, confidencial e baseado em dados para a escuta e o acompanhamento de situações sensíveis no cotidiano corporativo.

A arquitetura do sistema está estruturada em módulos bem definidos, utilizando **Python com Django** como framework base no backend. A comunicação entre as camadas é realizada por meio de APIs RESTful. O frontend poderá ser desenvolvido com **HTML/CSS/JavaScript**), e o banco de dados será gerenciado com **PostgreSQL**.

### 🔧 Tecnologias Utilizadas

| Camada         | Tecnologias                          |
|----------------|--------------------------------------|
| Backend        | Python, Django               |
| Frontend       | HTML5, CSS3, JavaScript (Bootstrap)   |
| Banco de Dados | PostgreSQL                           |
| Hospedagem     | A definir     |

---

A seguir, são apresentados os módulos desenvolvidos a partir dos processos identificados. Cada tabela representa um processo com os respectivos campos e características da interface.

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

![Blank diagram](https://github.com/user-attachments/assets/79cbe382-1890-455a-bf99-2edae65b3333)

---

### 4.2. Protótipos de telas

### Tela 01: Tela de login do usuário
A tela de login é o ponto de entrada da plataforma, garantindo um acesso restrito e seguro. Nesta interface, não há opção de cadastro direto, respeitando a política da plataforma de permitir apenas o ingresso de usuários vinculados a empresas previamente cadastradas pelo RH Connect. Isso assegura o controle de acesso e a confiabilidade da base de usuários. A interface foi projetada para ser objetiva, com um design limpo e centrado no campo de autenticação, atendendo aos requisitos de usabilidade e segurança.
![Tela de login](https://github.com/user-attachments/assets/3c2d2e72-2e69-436c-bd97-5a8464afa178)

### Tela 02: Home do painel administrativo (usuário master)
A home administrativa fornece uma visão centralizada para o usuário master (administrador da empresa ou da própria plataforma RH Connect). Esta interface permite o acesso rápido a módulos essenciais como empresas, colaboradores, chamados e relatórios. A organização das opções permite uma navegação fluida, apoiando a rotina dos gestores de RH e facilitando o monitoramento e as ações estratégicas com base em dados.
![Home - painel adm](https://github.com/user-attachments/assets/fffb0abd-a65a-4010-88d2-6670046119eb)

### Tela 03: Painel de empresas cadastradas
Essa interface apresenta a listagem de todas as empresas registradas na plataforma, incluindo funcionalidades como filtros, busca por nome e ações administrativas (editar ou remover). Essa tela foi pensada especialmente para os administradores da RH Connect, permitindo o gerenciamento eficiente das organizações participantes. Esse controle é essencial para garantir que apenas empresas verificadas possam utilizar o sistema.
![Home - empresas](https://github.com/user-attachments/assets/8700d6fd-ba73-4f64-8efb-68b68491d83b)

### Tela 04: Cadastro de empresa
A tela de cadastro de empresa é responsável por registrar novas empresas contratantes. São exigidos dados básicos, como nome, CNPJ, e-mail e domínio corporativo, além da seleção de plano de uso. Essa estrutura reforça a segurança, impedindo acessos de usuários externos ou não autorizados. Uma vez cadastrada, a empresa poderá gerenciar seus próprios colaboradores e chamados.
![Criar empresa](https://github.com/user-attachments/assets/ef5c6beb-b1b6-4230-ba51-41bf25846ca3)

### Tela 05: Painel de colaboradores cadastrados
Dentro do contexto de uma empresa, esse painel lista todos os colaboradores registrados, com filtros por nome, setor, status e data de cadastro. A exibição clara das informações permite que o psicólogo organizacional, como Lucas, tenha uma visão geral de sua base de colaboradores, podendo identificar padrões e necessidades de intervenção.
![Home - colaboradores](https://github.com/user-attachments/assets/345ee61c-a9a3-415a-9164-52f0da7be867)

### Tela 06: Cadastro de colaboradores
A tela de cadastro de colaboradores possibilita a inclusão manual ou em lote (via planilha) de funcionários. A partir desse cadastro, o sistema gera o primeiro acesso para o colaborador, de forma controlada. Esse fluxo garante que apenas usuários vinculados à empresa tenham acesso à plataforma, protegendo a integridade dos dados.
![Criar colaborador](https://github.com/user-attachments/assets/2f1f936a-50b5-4269-8931-62af967216a9)

### Tela 07: Home do usuário (colaborador)
Essa tela é o ponto de entrada dos colaboradores como Carlos. Aqui, ele encontra um ambiente amigável, com foco no seu bem-estar. A interface permite fácil navegação para abrir chamados, verificar seu histórico, atualizar dados pessoais e consultar respostas recebidas. O design foi desenvolvido para transmitir acolhimento e confiança, incentivando a abertura emocional.
![Home - usuário](https://github.com/user-attachments/assets/20c80f3d-9592-4c3f-bcc0-e04d81046bb4)

### Tela 08: Cadastro de chamados
Uma das telas mais sensíveis da plataforma, o formulário de abertura de chamados foi construído com foco na privacidade e no anonimato. O colaborador pode selecionar a categoria do problema, descrever sua situação e optar pelo envio anônimo. Essa funcionalidade responde diretamente à necessidade de Carlos, que deseja relatar questões emocionais sem o receio de represálias ou julgamentos.
![Criar chamado](https://github.com/user-attachments/assets/5a2c64b1-ca07-448d-9f1b-de11c83e8c86)

### Tela 09: Detalhes do usuário
Esta tela fornece informações pessoais do colaborador e histórico de chamados. Ela é acessada por ele próprio ou, com permissões específicas, por profissionais de RH. A centralização dessas informações permite uma comunicação mais efetiva e ações mais personalizadas por parte da equipe de apoio.
![Detalhes do usuário](https://github.com/user-attachments/assets/bc595054-6b52-4813-8edb-31b081868802)

### Tela 10: Dashboard - relatórios e métricas
Para o psicólogo organizacional, o acesso a dados é essencial para justificar iniciativas e validar resultados. Esta tela apresenta um painel de métricas como número de chamados abertos, chamados por setor, picos de uso, entre outros. Essas informações são importantes para transformar ações de bem-estar em argumentos estratégicos dentro da empresa.
![Dashboard - Relatorios e métricas](https://github.com/user-attachments/assets/53d64eb3-8a9a-4ab5-95c6-9dd3c24445c1)

### Tela 11: Construção de relatório 
Essa interface complementa o dashboard, permitindo ao usuário master criar relatórios personalizados com base em filtros como período, categoria, colaborador, e tipo de chamado. A construção flexível desses relatórios permite que o RH adapte suas análises conforme a demanda interna.
![Construção de relatório](https://github.com/user-attachments/assets/e6cad993-55d5-494e-8a87-eb50aa6c1aea)

### Tela 12: Detalhes do chamado
Essa tela exibe todas as informações referentes a um chamado aberto, incluindo histórico de comunicação, status e ações tomadas. Ela possibilita a resposta direta ao colaborador (quando identificado) ou o registro de observações internas. Essa interface é essencial para o acompanhamento cuidadoso e humanizado dos casos, sem perder a rastreabilidade e a eficiência do processo.
![Detalhes do chamado](https://github.com/user-attachments/assets/64f48942-173a-4ae5-b679-94134550f272)

### Conclusão
A construção das interfaces da plataforma RH Connect foi orientada pelas histórias reais de uso. Lucas, o psicólogo de RH, encontra nas funcionalidades da plataforma um apoio direto para implementar estratégias de cuidado emocional, com base em dados reais e acessíveis. Carlos, por outro lado, encontra uma oportunidade de ser ouvido com segurança, promovendo uma cultura de acolhimento e respeito. A união de design intuitivo, navegação simples, funcionalidades sensíveis e dados protegidos sustenta o compromisso da RH Connect com o bem-estar corporativo e a transformação dos ambientes de trabalho.

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

