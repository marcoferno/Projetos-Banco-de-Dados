#\\TESTE SIMPLES DE CONEXÃO COM O BANDO DE DADOS//#

import os
from scripts.database import conectar_bd

def teste_conexao_bd():
    conn = conectar_bd()
    assert conn is not None
    if conn:
        conn.close()
    else:
        print("Falha na conexão com o banco de dados.")

if __name__ == "__main__":
    teste_conexao_bd()