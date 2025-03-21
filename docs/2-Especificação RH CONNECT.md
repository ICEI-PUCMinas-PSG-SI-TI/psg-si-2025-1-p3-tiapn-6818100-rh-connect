# Especificações do Projeto

<span style="color:red">Pré-requisitos: <a href="01-Documentação de Contexto.md"> Documentação de Contexto</a></span>

Definição do problema e ideia de solução a partir da perspectiva do usuário. É composta pela definição do  diagrama de personas, histórias de usuários, requisitos funcionais e não funcionais além das restrições do projeto.

Apresente uma visão geral do que será abordado nesta parte do documento, enumerando as técnicas e/ou ferramentas utilizadas para realizar a especificações do projeto

## Personas
 Persona 1: Psicólogo de RH - Lucas Mendes 
- *Idade:* 35 anos  
- *Profissão:* Psicólogo Organizacional  
- *Formação:* Psicologia com especialização em Gestão de Pessoas  
- *Tempo de Experiência:* 10 anos atuando no setor de RH  
- *Motivações:*  
  - Promover um ambiente de trabalho saudável e acolhedor.  
  - Identificar e tratar problemas de saúde mental dos colaboradores de maneira ágil e eficiente.  
  - Desenvolver programas de bem-estar e reduzir índices de absenteísmo e rotatividade.  

- *Desafios:*  
  - Dificuldade em obter informações precisas e detalhadas sobre o estado emocional dos colaboradores.  
  - Falta de ferramentas práticas e seguras para o recebimento de chamados de saúde mental.  
  - Manter a confidencialidade e a confiança dos funcionários no processo de abertura de chamados.  

- *Necessidades:*  
  - Sistema seguro e intuitivo para receber chamados e denúncias.  
  - Relatórios gerenciais para identificar padrões e criar estratégias de intervenção.  
  - Canal de comunicação direta com colaboradores, mantendo a confidencialidade.  

-----

*Persona 2: Operador de Produção - Carlos Silva*  
- *Idade:* 28 anos  
- *Profissão:* Operador de Produção em uma indústria de alimentos  
- *Formação:* Ensino Médio completo  
- *Tempo de Experiência:* 6 anos na empresa atual  
- *Motivações:*  
  - Manter um bom desempenho e garantir estabilidade no emprego.  
  - Sentir-se valorizado e acolhido pela empresa, especialmente em momentos de estresse e pressão.  
  - Ter um canal seguro para relatar dificuldades emocionais e problemas no ambiente de trabalho.  

- *Desafios:*  
  - Sentir-se confortável para relatar problemas sem medo de represálias.  
  - Encontrar suporte emocional para lidar com estresse e sobrecarga de trabalho.  
  - Comunicar problemas ao RH de maneira prática e segura.  

- *Necessidades:*  
  - Garantia de anonimato ao relatar dificuldades.  
  - Facilidade de acesso ao sistema para abertura de chamados.  
  - Acompanhamento da resolução de problemas com retorno claro e objetivo.  


## Histórias de Usuários

Com base na análise das personas forma identificadas as seguintes histórias de usuários:

História da Persona 1: 
Lucas Mendes é um psicólogo organizacional de 35 anos que sempre sonhou em fazer a diferença na vida das pessoas por meio do trabalho. Com uma década de experiência no setor de RH e uma especialização em Gestão de Pessoas, ele acredita que o ambiente corporativo pode ser um local saudável e acolhedor. Sua paixão é desenvolver iniciativas que promovam o bem-estar dos colaboradores, reduzindo índices de absenteísmo e rotatividade.

Apesar de sua dedicação, Lucas enfrenta desafios. Ele percebe a necessidade urgente de ferramentas práticas e seguras para acessar informações sobre o estado emocional dos colaboradores sem comprometer a confidencialidade. Ele se preocupa em manter a confiança dos funcionários no processo e frequentemente busca novas soluções para superar essas dificuldades. Além disso, sente o peso de atender às expectativas da liderança enquanto mantém o equilíbrio entre métricas e o cuidado humano.

Em seu dia a dia, Lucas organiza palestras, workshops e programas voltados à saúde mental e bem-estar. Ele sonha em ser reconhecido como um líder transformador e em mostrar, por meio de relatórios detalhados, que suas ações realmente fazem diferença. No fundo, seu maior objetivo é criar um ambiente corporativo onde todos se sintam apoiados emocionalmente e engajados.

História da Persona 2:
Carlos Silva tem 28 anos e trabalha como operador de produção em uma indústria de alimentos. Ele é conhecido entre seus colegas por ser dedicado e esforçado, sempre buscando manter um bom desempenho e garantir a estabilidade no emprego. Com seis anos de experiência na empresa, Carlos valoriza a oportunidade de ter crescido no setor, mas sente que a rotina é cada vez mais estressante.

Carlos enfrenta desafios diários. Em um ambiente de alta pressão, ele percebe a dificuldade em relatar problemas emocionais ao RH sem medo de represálias. Muitas vezes, ele prefere desabafar com colegas de confiança, mas sente falta de um canal seguro e anônimo onde possa expor suas dificuldades de maneira prática.

Além de lidar com o estresse no trabalho, Carlos também busca por reconhecimento e apoio por parte da empresa. Ele acredita que, com suporte adequado, sua produtividade e bem-estar poderiam ser ainda melhores. Seu sonho é trabalhar em um ambiente onde as demandas sejam equilibradas e ele se sinta acolhido e valorizado.

No fim do dia, Carlos quer mais do que apenas um salário: ele busca um trabalho que não comprometa sua saúde mental e emocional, enquanto constrói uma relação de confiança e respeito com seus empregadores.

|EU COMO... `PERSONA`| QUERO/PRECISO ... `FUNCIONALIDADE` |PARA ... `MOTIVO/VALOR`                 |
|--------------------|------------------------------------|----------------------------------------|
|Psicólogo de RH  | Descobrir problemas dos colaboradores         | Melhorar o bem estar coorporativo          |
|Operador de Produção  | Falar/abrir chamados sobre o ambiente coorporativo  | Manter o bem estar coorporativo |


## Requisitos

As tabelas que se seguem apresentam os requisitos funcionais e não funcionais que detalham o escopo do projeto. Para determinar a prioridade de requisitos, aplicar uma técnica de priorização de requisitos e detalhar como a técnica foi aplicada.

### Requisitos Funcionais

|ID    | Descrição do Requisito  | Prioridade |
|------|-----------------------------------------|----|
|RF-001| Permitir que o usuário abra chamado | ALTA | 
|RF-002| Encaminhar a demanda ao setor responsavel  | ALTA |
|RF-003| Sistema tem que ser usual  | ALTA |
|RF-003| Permitir que o usuário abra chamado de forma anonima  | Média |

### Requisitos não Funcionais

|ID     | Descrição do Requisito  |Prioridade |
|-------|-------------------------|----|
|RNF-001| O sistema deve ser responsivo para rodar em um dispositivos móvel | BAIXA | 
|RNF-002| O sistema deve ser interativo  | BAIXA | 


## Restrições

O projeto está restrito pelos itens apresentados na tabela a seguir.

|ID| Restrição                                             |
|--|-------------------------------------------------------|
|01| O projeto deverá ser entregue até o final do semestre |
|02| Não pode ser desenvolvido um módulo de backend        |

Enumere as restrições à sua solução. Lembre-se de que as restrições geralmente limitam a solução candidata.

> **Links Úteis**:
> - [O que são Requisitos Funcionais e Requisitos Não Funcionais?](https://codificar.com.br/requisitos-funcionais-nao-funcionais/)
> - [O que são requisitos funcionais e requisitos não funcionais?](https://analisederequisitos.com.br/requisitos-funcionais-e-requisitos-nao-funcionais-o-que-sao/)
