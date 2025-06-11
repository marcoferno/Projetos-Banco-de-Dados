# 🎬 Projeto IMDB + OMDb API

Um projeto Python completo que integra a [OMDb API](https://www.omdbapi.com/) com um banco de dados MySQL relacional para armazenar filmes, diretores, atores e gêneros de forma automatizada e escalável.

---

## 📁 Estrutura do Projeto

```
IMDB/
├── scripts/                   # Lógica principal
│   ├── database.py            # Conexão com MySQL
│   ├── manipulador_dados.py  # Utilitários de inserção
│   ├── omdb_fetcher.py        # Integração OMDb + BD
│   └── utils.py               # Logger, safe_int/float, validador
├── testes/                    # Testes automatizados
│   ├── teste_api.py
│   ├── teste_api_mock.py
│   ├── teste_bd.py
│   ├── teste_insercao.py
│   ├── teste_insercao_mock.py
│   └── teste_manipulador_dados.py
├── .env                       # Variáveis de ambiente (OMDB_API_KEY)
├── IMDB.sql                   # Script SQL para criar o banco
└── README.md
```

---

## 🚀 Funcionalidades

- 🔍 Busca dados de filmes via OMDb API
- 🗃️ Insere no banco MySQL relacional:
  - Filmes
  - Diretores (e relacionamento)
  - Atores (e relacionamento)
  - Gêneros (e relacionamento)
- 🔁 Reutiliza dados (evita duplicatas)
- 🧪 Possui testes com e sem mock
- 🧠 Usa tratamento seguro de dados e loggers

---

## ⚙️ Requisitos

- Python 3.9+
- MySQL Server
- Pacotes:
  - `mysql-connector-python`
  - `requests`
  - `python-dotenv`
  - `pytest`

Instalar com:
```bash
pip install -r requirements.txt
```
---

## 🔐 Configuração

Crie um arquivo `.env` na raiz com:
```env
OMDB_API_KEY=your_api_key_here
```

---

## 🛠️ Como usar

### Inserir manualmente um filme:
```bash
python scripts/omdb_fetcher.py
```
Digite o nome do filme quando solicitado.

---

## 🧪 Rodar os testes

```bash
pytest testes/ -v
```

Testes incluem:
- API real e mockada
- Inserção no banco (real e mock)
- Manipulação de dados (isolado)

---

## 🗃️ Banco de Dados

Use `IMDB.sql` para criar as tabelas.

### Principais tabelas:
- `Filmes`
- `Atores`, `Diretor`, `Generos`
- `Atores_do_Filme`, `Diretores_do_Filme`, `Genero_do_Filme`

Todas com **chaves estrangeiras** para integridade referencial.

### 📊 Diagrama Relacional

![Image](https://github.com/user-attachments/assets/51accfb4-08ab-437e-acdf-4ef687f1821f)

---

## ✨ Destaques

- Modularidade limpa e testável
- Logger informativo e estruturado
- Funções auxiliares reutilizáveis (safe casting, validação)
- Pronto para CI/CD com mocks
