import psycopg
from psycopg.rows import dict_row

def conectar():
    return psycopg.connect(
        host="localhost",
        dbname="northwind",
        user="postgres",
        password="1234",
        row_factory=dict_row
    )
