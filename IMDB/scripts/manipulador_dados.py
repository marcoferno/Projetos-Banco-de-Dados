#\\MÓDULOS DE MANIPULAÇÃO//#

def tratar_campo_lista (campo):
    if not campo or campo == 'N/A':
        return []
    return [item.strip() for item in campo.split(',') if item.strip() != 'N/A']

def obter_ou_criar(cursor, tabela, coluna, valor):
    id_columns = {
        'Atores': 'ID_Ator',
        'Diretor': 'ID_Diretor',
        'Generos': 'ID_Genero'
    }

    id_coluna = id_columns.get(tabela, f"ID_{tabela}")

    cursor.execute(f"SELECT {id_coluna} FROM {tabela} WHERE {coluna} = %s", (valor,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    cursor.execute(f"INSERT INTO {tabela} ({coluna}) VALUES (%s)", (valor,))

    return cursor.lastrowid

