# Crypto Fear & Greed Index Scraper

Este projeto realiza web scraping em dois sites para capturar os índices de "Crypto Fear & Greed" e "CBBI Confidence Score". Ele coleta essas informações diariamente e exibe os valores no console. A ideia é depois enviar automaticamente por e-mail.

## Funcionalidades

- Acessa automaticamente os sites:
  - [Alternative.me - Fear & Greed Index](https://alternative.me/crypto/fear-and-greed-index/)
  - [Colin Talks Crypto - CBBI](https://colintalkscrypto.com/cbbi/)
- Coleta os valores dos índices e os imprime no console.
- Agenda a coleta para ser executada diariamente às 21:01.

## Tecnologias Utilizadas

- **Python 3**: Linguagem principal do projeto.
- **Selenium**: Usado para automação de navegação web e extração de dados.
- **webdriver-manager**: Gerencia o download automático do driver do navegador.
- **schedule**: Biblioteca para agendamento de tarefas.

## Requisitos

1. Python 3.7+
2. As dependências listadas no arquivo `requirements.txt`

## Configuração

1. Clone o repositório:
    ```bash
   git clone <URL_DO_REPOSITORIO>
   cd web_scraping_BITCOIN
   
2. Crie e ative um ambiente virtual:
    ```bash
   python -m venv .venv
   source .venv/bin/activate   # No Windows: .venv\Scripts\activate
   
3. Instale as dependências:
    ```bash
   pip install -r requirements.txt

4. Execute a main:
    ```bash
   python main.py
   
## Autor
Desenvolvido por Gabriel Noronha: https://www.linkedin.com/in/gabriel-noronha-151940277/
