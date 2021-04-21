import pyodbc

class Bacon():
    def __init__(self):
        server = 'DESKTOP-O0728HG\SQLEXPRESS'
        database = 'PROJETORH'
        string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
        c = pyodbc.connect(string_conexao)
        self.cur = c.cursor()

    def consulta(self):
        show = self.cur.execute(f'''
                   select * from DEMISSIONAL
                   ''')
        for i in show:
            print(i)
            return print(i)

    def Cadastra(self):
        self.cur.execute(f'''

''')


