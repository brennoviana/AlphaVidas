# ChatProject

Este é um projeto de exemplo que combina um backend Django com FastAPI e um frontend baseado em React.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em sua máquina:

- Python 3.10 ou superior
- Node.js e npm

## Configuração do Backend

1. Clone o repositório e navegue até o diretório do projeto:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd ChatProject
    ```

2. Ative o docker-compose:

    ```bash
    docker-compose up -d
    ```

3. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv
    ```

4. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```

5. Instale as dependências do backend:
    ```bash
    pip install -r requirements.txt
    ```

6. Execute as migrações e inicie o servidor Django:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

7. Navegue até o diretório do backend:
    ```bash
    cd ChatProject/backend
    ```

8. Execute o servidor FastAPI:
    ```bash
    uvicorn main:app --reload --port 8080
    ```

## Configuração do Frontend

1. Navegue até o diretório do frontend:
    ```bash
    cd ChatProject/frontend
    ```

2. Instale as dependências do frontend:
    ```bash
    npm install
    ```

3. Inicie o servidor de desenvolvimento do React:
    ```bash
    npm run start
    ```

## Acessando o Projeto

1. Acesse a aplicação Django em seu navegador:
    ```
    http://localhost:8000
    ```

2. Acesse a aplicação React em seu navegador:
    ```
    http://localhost:3000
    ```

## Resumo

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`
- `cd ChatProject/backend`
- `uvicorn main:app --reload --port 8080`
- `cd ../frontend`
- `npm install`
- `npm run start`

## Notas

Certifique-se de manter o ambiente virtual ativado sempre que estiver trabalhando no projeto para garantir que todas as dependências estejam disponíveis.
