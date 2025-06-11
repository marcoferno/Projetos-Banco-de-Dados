#\\TESTE DE MANIPULAÇÃO DE DADOS//#

import pytest
from scripts.manipulador_dados import tratar_campo_lista, obter_ou_criar
from unittest.mock import MagicMock

def teste_tratar_campo_lista_normal():
    assert tratar_campo_lista("A, B, C") == ["A", "B", "C"]

def teste_tratar_campo_lista_vazio():
    assert tratar_campo_lista("") == []

def teste_tratar_campo_lista_na():
    assert tratar_campo_lista("N/A") == []

def teste_tratar_campo_lista_com_na_misto():
    assert tratar_campo_lista(" A , N/A , B ") == ["A", "B"]

# Testes para obter_ou_criar() com mock
def teste_obter_ou_criar_existente():
    cursor = MagicMock()
    cursor.fetchone.return_value = (42,)  # Simula que já existe

    resultado = obter_ou_criar(cursor, "Atores", "Nome", "Teste Ator")

    cursor.execute.assert_called_with(
        "SELECT ID_Ator FROM Atores WHERE Nome = %s", ("Teste Ator",)
    )
    assert resultado == 42

def teste_obter_ou_criar_novo():
    cursor = MagicMock()
    cursor.fetchone.return_value = None  # Simula que não existe

    def falsa_execucao(query, params):
        if query.startswith("INSERT"):
            cursor.lastrowid = 99
    cursor.execute.side_effect = falsa_execucao

    resultado = obter_ou_criar(cursor, "Atores", "Nome", "Novo Ator")

    assert resultado == 99