#\\TESTE DE CONEXÃO FETCH DA API//#

from scripts.omdb_fetcher import fetch_api

def teste_fecth_api():
    titulo = "Inception"
    dados = fetch_api(titulo)
    if dados:
        print("Filme encontrado!")
        print(f"Título: {dados.get('Title')}")
        print(f"Ano: {dados.get('Year')}")
        print(f"Diretor: {dados.get('Director')}")
    else:
        print("Filme não encontrado ou erro na requisição.")

if __name__ == "__main__":
    teste_fecth_api()
