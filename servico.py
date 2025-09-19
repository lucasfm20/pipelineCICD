import sqlite3
def conectar_banco():
    conn = sqlite3.connect(':memory:') # Banco in-memory para testes
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT)')
    return conn, cursor
def cadastrar_usuario(nome):
    conn, cursor = conectar_banco()
    cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
    conn.commit()
    cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    return cursor.fetchone()