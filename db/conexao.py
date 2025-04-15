import psycopg
from psycopg.rows import dict_row

def conectar():
    return psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="admin",
        row_factory=dict_row
    )
