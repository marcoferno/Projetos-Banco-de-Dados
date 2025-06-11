#\\TESTE DE INSERÇÃO DE DADOS NO BD (MOCK)//#

from unittest.mock import patch
from scripts.omdb_fetcher import inserir_dados_filmes
from scripts.database import conectar_bd

mock_response = {
    'Title': 'The Matrix',
    'Year': '1999',
    'Director': 'Lana Wachowski, Lilly Wachowski',
    'Actors': 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss',
    'Genre': 'Action, Sci-Fi',
    'Runtime': '136 min',
    'imdbRating': '8.7',
    'imdbVotes': '1,700,000',
    'Plot': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
    'Poster': 'https://linkdaposter.com/thematrix.jpg',
    'Metascore': '73',
    'Rated': 'R',
    'Response': 'True'
}

@patch('scripts.omdb_fetcher.fetch_api')
def teste_insercao_dados_mock(mock_fetch):

    mock_fetch.return_value = mock_response

    filme = mock_fetch('The Matrix')

    assert filme is not None
    assert filme['Title'] == 'The Matrix'

    inserir_dados_filmes(filme)

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Filmes WHERE Titulo = %s", (filme['Title'],))
    resultado = cursor.fetchone()

    assert resultado is not None
    print("Filme inserido com sucesso no banco!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    teste_insercao_dados_mock()