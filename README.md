# API Connect

API REST para cadastro e consulta de usuários.

## Objetivo

O projeto consiste no desenvolvimento de uma API REST para gerenciamento de usuários. A aplicação recebe requisições HTTP, processa os dados e retorna respostas no formato JSON.

## Tecnologias

- Python
- Flask
- JSON
- API REST
- Git
- GitHub
- GitHub Codespaces
- Postman

## Execução do projeto

### Pré-requisitos

- Python 3 instalado
- Git
- Acesso ao terminal

### Iniciar a aplicação

No terminal, dentro da pasta do projeto, execute:

    python app.py

Após iniciar, a aplicação ficará disponível na porta 5000.

    http://127.0.0.1:5000

## Endpoints

| Método | Endpoint | Descrição | Status |
|---|---|---|---|
| GET | `/` | Verifica o funcionamento da API | 200 |
| POST | `/usuarios` | Cadastra um usuário | 201 |
| GET | `/usuarios` | Lista os usuários cadastrados | 200 |
| GET | `/usuarios/<id>` | Consulta um usuário pelo ID | 200 / 404 |

## Exemplos de requisições

### Verificar a API

**GET `/`**

Resposta:

    {
      "mensagem": "API Connect em funcionamento."
    }

**Status:** 200 OK

### Cadastrar usuário

**POST `/usuarios`**

Corpo:

    {
      "nome": "Maria Silva",
      "email": "maria@email.com"
    }

**Status:** 201 Created

### Cadastrar usuário sem e-mail

**POST `/usuarios`**

Corpo:

    {
      "nome": "João Silva"
    }

Resposta:

    {
      "error": "Os campos nome e email são obrigatórios."
    }

**Status:** 400 Bad Request

### Listar usuários

**GET `/usuarios`**

Resposta:

    {
      "data": [
        {
          "id": 1,
          "nome": "Maria Silva",
          "email": "maria@email.com"
        }
      ]
    }

**Status:** 200 OK

### Consultar usuário inexistente

**GET `/usuarios/9999`**

Resposta:

    {
      "error": "Usuário não encontrado.",
      "id_solicitado": 9999
    }

**Status:** 404 Not Found

## Testes realizados

Os testes da API foram realizados utilizando o Postman.

| Cenário | Método | Endpoint | Resultado |
|---|---|---|---|
| Cadastro com sucesso | POST | `/usuarios` | 201 Created |
| Cadastro sem e-mail | POST | `/usuarios` | 400 Bad Request |
| Listagem de usuários | GET | `/usuarios` | 200 OK |
| Usuário inexistente | GET | `/usuarios/9999` | 404 Not Found |

## Estrutura do projeto

    api-connect/
    ├── app.py
    ├── README.md
    └── ...

## Autora

Cristiane Moraes