import cx_Oracle
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")

    # ✅ Use direct IP instead of hostname
    dsn = cx_Oracle.makedsn("192.168.56.50", 1521, service_name="pdbprim1")

    conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)
    return conn
