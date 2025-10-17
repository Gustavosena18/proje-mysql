# CRUD com Mqsql + python + streamlit

Este projeto é um exemplo prático de CRUD usando:

- Banco de dados **MYSQL**
- Conexão com o **mysql.connector**
- Interface web com **streamlit**

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/Gustavosena18/proje-mysql.git
```

## 2. Instalar dependências 
```bash
pip install -r requirements.tmt
```

## 3. Configurar as variáveis de ambiente

Crie um arquivo .env na raiz do seu projeto com:
```bash
DB_NAME=seu_DB
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOSt=localhost
```

### 4. Rodar aplicação
```bash
python -m streamlit run app.py
```

### 5. Funcionalidades

- Inserrir registos no db

- Listar registros no db 

- Atualizar registro no db

- Deletar reistros no db 

- Inteerface simples com Streamlit

