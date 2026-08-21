# API Connect

API REST para cadastro e consulta de usuários.

## 1. Objetivo

O projeto consiste no desenvolvimento de uma API REST para gerenciamento de usuários. A aplicação recebe requisições HTTP, processa os dados e retorna respostas no formato JSON.

## 2. Tecnologias utilizadas

- Python
- Flask
- JSON
- HTTP/REST
- Git
- GitHub
- GitHub Codespaces
- Postman

## 3. Execução do projeto

### Pré-requisitos

- Python 3
- Git
- Acesso ao terminal

### Inicialização

No terminal, dentro da pasta do projeto, execute:

    python app.py

Após a inicialização, a aplicação será executada na porta 5000.

    http://127.0.0.1:5000

## 4. Endpoints

| Método | Endpoint | Descrição | Status esperado |
|---|---|---|---|
| GET | `/` | Verifica o funcionamento da API | 200 |
| POST | `/usuarios` | Cadastra um novo usuário | 201 |
| GET | `/usuarios` | Lista os usuários cadastrados | 200 |
| GET | `/usuarios/<id>` | Consulta um usuário pelo ID | 200 / 404 |

## 5. Exemplos de requisições

### 5.1 Verificar o funcionamento da API

**Método:** GET

**Endpoint:** `/`

Resposta:

    {
      "mensagem": "API Connect em funcionamento."
    }

**Status HTTP:** 200 OK

### 5.2 Cadastrar usuário

**Método:** POST

**Endpoint:** `/usuarios`

Corpo da requisição:

    {
      "nome": "Maria Silva",
      "email": "maria@email.com"
    }

Resposta:

    {
      "data": {
        "id": 1,
        "nome": "Maria Silva",
        "email": "maria@email.com"
      }
    }

**Status HTTP:** 201 Created

### 5.3 Cadastrar usuário sem e-mail

**Método:** POST

**Endpoint:** `/usuarios`

Corpo da requisição:

    {
      "nome": "João Silva"
    }

Resposta:

    {
      "error": "Os campos nome e email são obrigatórios."
    }

**Status HTTP:** 400 Bad Request

### 5.4 Listar usuários

**Método:** GET

**Endpoint:** `/usuarios`

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

**Status HTTP:** 200 OK

### 5.5 Consultar usuário inexistente

**Método:** GET

**Endpoint:** `/usuarios/9999`

Resposta:

    {
      "error": "Usuário não encontrado.",
      "id_solicitado": 9999
    }

**Status HTTP:** 404 Not Found

## 6. Testes realizados

Os testes da API foram realizados utilizando o Postman, contemplando cenários de sucesso e de validação de erros.

| Cenário | Método | Endpoint | Resultado |
|---|---|---|---|
| Cadastro com sucesso | POST | `/usuarios` | 201 Created |
| Cadastro sem e-mail | POST | `/usuarios` | 400 Bad Request |
| Listagem de usuários | GET | `/usuarios` | 200 OK |
| Usuário inexistente | GET | `/usuarios/9999` | 404 Not Found |

## 7. Estrutura do projeto

    api-connect/
    ├── controllers/
    ├── data/
    ├── routes/
    ├── app.py
    └── README.md

## 8. Autora

Cristiane Moraes
