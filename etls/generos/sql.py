import sqlite3
from sqlite3 import Connection, Error

from models import Genero


def criar_conexao(caminho_do_sqlite: str) -> Connection:
    try:
        return sqlite3.connect(caminho_do_sqlite)
    except Error as e:
        raise e


def executar_sql(query: str, conexao: Connection, args=None, commit=False, fetch=False):
    args = args or ()
    data = None
    cursor = conexao.cursor()
    cursor.execute(query, args)
    if commit:
        conexao.commit()
    if fetch:
        data = cursor.fetchall()
    return data


def inserir_genero(genero: Genero, conexao: Connection):
    sql = """ INSERT OR IGNORE INTO genero(nome) VALUES (?) """
    return executar_sql(
        conexao=conexao,
        query=sql,
        args=(genero.value,),
        commit=True,
    )
