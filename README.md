# Dashboard de Comunicação Interna - Startup Connect

Este projeto é um protótipo funcional de um Dashboard de Comunicação Interna, desenvolvido para validar a viabilidade técnica de uma interface que consome dados de uma API RESTful externa (JSONPlaceholder) em uma arquitetura de microserviços.

## 1. Engenharia de Requisitos
### Histórias de Usuário (User Stories)
- **User Story 1:** Como funcionário, desejo ver uma lista de colegas para facilitar o networking interno.
- **User Story 2:** Como colaborador, desejo visualizar as postagens recentes para me manter atualizado sobre os avisos da empresa.
- **User Story 3:** Como usuário, desejo que o sistema me avise caso a internet esteja lenta ou caia, em vez de travar.
- **User Story 4:** Como gestor, desejo visualizar o número total de posts por usuário para acompanhar o engajamento.

### Requisitos Não-Funcionais
- **Resiliência:** O sistema deve ser tolerante a falhas de rede e indisponibilidade da API externa.
- **Desempenho:** As requisições devem possuir um tempo limite (timeout) para evitar o travamento da aplicação (estratégia de fail-fast).

## 2. Arquitetura e Padrão de Projeto
O projeto utiliza a arquitetura **Cliente-Servidor**. O cliente Python consome recursos via verbos HTTP (GET) de uma API baseada em nuvem. 

A organização do código segue o padrão **MVC (Model-View-Controller)**:
- **Model:** Representado pelas classes de domínio que estruturam os dados recebidos em JSON.
- **View:** Interface de linha de comando (CLI) que renderiza os dados para o usuário final.
- **Controller:** Lógica centralizada que orquestra as requisições, o tratamento de dados e o fluxo da aplicação.

## 3. Modelagem Estrutural (UML)
A estrutura de dados foi planejada para suportar a multiplicidade de relações entre entidades da startup.
- **Associação 1:N:** Um Usuário pode possuir múltiplas Postagens associadas ao seu ID.

[Insira aqui a imagem do seu diagrama: diagrama_classes.png]

## 4. Gerenciamento de Riscos (Resiliência)
- **Estratégia de Mitigação:** Implementação de blocos `try/except` para captura de exceções de rede e erros HTTP (como 404 ou 500).
- **Timeouts:** Configuração de limite de resposta de 5 segundos para garantir que a aplicação permaneça responsiva mesmo sob condições adversas de rede.

## 5. Processo de Planejamento (Apresentação do PRD)
Como parte da estratégia de prototipagem rápida da startup, utilizamos Inteligência Artificial para auxiliar na estruturação dos requisitos e documentação.

**Prompt Principal utilizado:**
> "Atue como um Engenheiro de Software Sênior. Preciso criar o PRD para um Dashboard de Comunicação Interna que consome a API JSONPlaceholder. Gere User Stories, um Diagrama de Classes UML descritivo, explique a aplicação do padrão MVC e defina estratégias de resiliência (Timeout e Try/Catch) para falhas na API."

---