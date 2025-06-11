#\\MÓDULOS DE CONFIGURAÇÃO//#

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv('BD_HOST'),
            user=os.getenv('BD_USER'),
            password=os.getenv('BD_PASSWORD'),
            database=os.getenv('BD_NAME')
        )
        if conexao.is_connected():
            print("Sucesso ao conectar com o banco de dados")
        return conexao
    except Error as e:
        print(f"Erro na conexão com o banco de dados: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None
