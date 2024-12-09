import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=empresa_gestao;'
        'UID=sa;'
        'PWD=sua_senha'
    )
    return conn
