import cx_Oracle

def get_connection():
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="pdbprim1")
    conn = cx_Oracle.connect(user="BOOKVAULT_USER", password="b1", dsn=dsn)
    return conn
