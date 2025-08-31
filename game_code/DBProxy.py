import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        # conecta no banco de dados (se não existir, cria)
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL, score INTEGER NOT NULL, date TEXT NOT NULL)''')

    # insere um novo registro na tabela usando os dados do dicionário
    def save(self, score_dict: dict):
        self.connection.execute('''INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)''', score_dict)
        self.connection.commit()  # salva as mudanças no banco

    # pega os 5 maiores scores do banco e devolve numa lista
    def retrieve_top5(self) -> list:
        return self.connection.execute('''SELECT * FROM dados ORDER BY score DESC LIMIT 5''').fetchall()

    # fecha a conexão com o banco de dados
    def close(self):
        return self.connection.close()
