import sqlite3

# Criando a tabela e inserindo dados - CREATE
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Contatos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   email TEXT,
                   telefone TEXT)
            ''')

dadosExemplo = [
    ('João', 'joao@email.com', '123-4356-7890'),
    ('Marcelo', 'marcelo@email.com', '987-654-3210'),
    ('Victoria', 'vic@email.com', '333-333-3333')
]

cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?,?,?)',
                   dadosExemplo)

# Leitura e exibição de dados da tabela - READ
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print("Contatos:")

for contato in contatos:
    print(contato)

# Atualizando dados da tabela, como e-mail, por exemplo - UPDATE
novoEmail = 'mar@email.com'
contatoId = 1

cursor.execute('UPDATE Contatos SET email = ? WHERE id = ?', (novoEmail, contatoId))
conn.commit()

# Exclusão de algum contato na tabela, como o ID 3, por exemplo - DELETE
contatoIdExcluir = 1

cursor.execute('DELETE FROM Contatos WHERE id = ?', (contatoIdExcluir,))
conn.commit()

# Leitura final para verificar alterações
cursor.execute('SELECT * FROM Contatos')
contatos_finais = cursor.fetchall()
print("\nContatos após atualizações:")
for contato in contatos_finais:
    print(contato)

conn.close()
