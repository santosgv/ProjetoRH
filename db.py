import pyodbc

server = 'DESKTOP-O0728HG\SQLEXPRESS'
database = 'PROJETORH'
string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
c = pyodbc.connect(string_conexao)
cur = c.cursor()


def consulta():
    show = cur.execute(f'''
           select * from DEMISSIONAL
           ''')
    for i in show:
        print(i)
    return print(i)