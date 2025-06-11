#\\MÓDULO DE CONEXÃO E BUSCA DE DADOS NA API//#

# scripts/omdb_fetcher.py

import mysql.connector
import requests
from requests.exceptions import RequestException
import os
from dotenv import load_dotenv
from scripts.database import conectar_bd
from scripts.manipulador_dados import tratar_campo_lista, obter_ou_criar
from scripts.utils import obter_logger, safe_int, safe_float, e_valido

load_dotenv()

API_KEY = os.getenv('OMDB_API_KEY')
URL = 'http://www.omdbapi.com/'
logger = obter_logger(__name__)

# FUNCIONALIDADE #1 - FETCH_API
def fetch_api(titulo):
    try:
        parametros = {'t': titulo, 'apikey': API_KEY}
        resposta = requests.get(URL, params=parametros, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        if dados.get('Response') == 'True':
            return dados
        else:
            logger.warning(f"Filme não encontrado na API: {titulo}")
            return None

    except RequestException as e:
        logger.error(f"Erro na requisição da API OMDb: {e}")
        return None
    except Exception as e:
        logger.error(f"Erro inesperado na função fetch_api: {e}")
        return None

# FUNCIONALIDADE #2 - INSERIR_DADOS_FILMES
def inserir_dados_filmes(dados):
    logger.info(f"Iniciando inserção do filme: {dados.get('Title')}")
    conn = conectar_bd()
    if not conn:
        logger.error("Conexão com banco falhou. Inserção abortada.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Filmes (Titulo, Ano, Imagem_URL, Certificado, Tempo_Filme, IMDB_Nota, Descricao, Metascore, Votos, Gross)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            dados.get('Title'),
            safe_int(dados.get('Year', '0').split('–')[0]),
            dados.get('Poster'),
            dados.get('Rated'),
            safe_int(dados.get('Runtime', '0 min').split(' ')[0]),
            safe_float(dados.get('imdbRating')),
            dados.get('Plot'),
            safe_int(dados.get('Metascore')),
            safe_int(dados.get('imdbVotes').replace(',', '')),
            None
        ))
        filme_id = cursor.lastrowid
        logger.info(f"Filme inserido com ID: {filme_id}")

        # Diretores
        diretores = tratar_campo_lista(dados.get('Director'))
        for diretor in diretores:
            diretor_id = obter_ou_criar(cursor, 'Diretor', 'Nome', diretor)
            cursor.execute("""
                INSERT INTO Diretores_do_Filme (Filmes_ID_Filmes, Diretor_ID_Diretor)
                VALUES (%s, %s)
            """, (filme_id, diretor_id))

        # Atores
        atores = tratar_campo_lista(dados.get('Actors'))
        for ator in atores:
            ator_id = obter_ou_criar(cursor, 'Atores', 'Nome', ator)
            cursor.execute("""
                INSERT INTO Atores_do_Filme (Filmes_ID_Filmes, Atores_ID_Ator)
                VALUES (%s, %s)
            """, (filme_id, ator_id))

        # Gêneros
        generos = tratar_campo_lista(dados.get('Genre'))
        for genero in generos:
            genero_id = obter_ou_criar(cursor, 'Generos', 'Nome', genero)
            cursor.execute("""
                INSERT INTO Genero_do_Filme (Filmes_ID_Filmes, Generos_ID_Genero)
                VALUES (%s, %s)
            """, (filme_id, genero_id))

        conn.commit()
        logger.info(f"Filme '{dados.get('Title')}' inserido com sucesso no banco de dados.")

    except mysql.connector.Error as e:
        conn.rollback()
        logger.error(f"Erro no banco de dados durante inserção: {e}")
    except Exception as e:
        conn.rollback()
        logger.error(f"Erro inesperado na inserção: {e}")
    finally:
        cursor.close()
        conn.close()
        logger.info("Conexão com banco encerrada.")

if __name__ == "__main__":
    titulo = input("Digite o nome do filme: ")
    filme = fetch_api(titulo)
    if filme:
        inserir_dados_filmes(filme)
