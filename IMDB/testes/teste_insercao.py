#\\TESTE DE INSERÇÃO DE DADOS NO BD//#

import pytest
from scripts.omdb_fetcher import fetch_api, inserir_dados_filmes
from scripts.database import conectar_bd

def teste_insercao_dados():
    titulo = 'Indiana Jones'
    filme = fetch_api(titulo)
    assert filme is not None

    inserir_dados_filmes(filme)

    conn = conectar_bd()
    cursor = conn.cursor()

    titulo_real = filme.get('Title')
    cursor.execute("SELECT * FROM Filmes WHERE Titulo = %s", (titulo_real,))
    result = cursor.fetchone()

    assert result is not None

    cursor.close()
    conn.close()