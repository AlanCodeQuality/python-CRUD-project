import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criar a tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Fechar a conexão com o banco de dados
conn.commit()
conn.close()

print("Database and table created successfully.")
