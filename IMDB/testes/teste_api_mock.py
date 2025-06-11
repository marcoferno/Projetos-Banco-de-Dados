#\\TESTE DE CONEXÃO FETCH DA API (MOCK)//#

from unittest.mock import patch
from scripts.omdb_fetcher import fetch_api

# Dados simulados que a API OMDb responderia
mock_response = {
    'Title': 'Inception',
    'Year': '2010',
    'Director': 'Christopher Nolan',
    'Actors': 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page',
    'Genre': 'Action, Adventure, Sci-Fi',
    'Runtime': '148 min',
    'imdbRating': '8.8',
    'imdbVotes': '2,000,000',
    'Plot': 'A thief who steals corporate secrets...',
    'Poster': 'https://linkdaposter.com/poster.jpg',
    'Metascore': '74',
    'Rated': 'PG-13',
    'Response': 'True'
}

@patch('scripts.omdb_fetcher.requests.get')

def teste_fecth_api_mock(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    resultado = fetch_api('Inception')

    assert resultado is not None
    assert resultado['Title'] == 'Inception'
    assert resultado['Director'] == 'Christopher Nolan'
    assert resultado['Year'] == '2010'
    print("Teste com mock da API executado com sucesso!")

if __name__ == "__main__":
    teste_fecth_api_mock()