import pyodbc

server = "sai-healthtech-server7418.database.windows.net"
database = "healthtech-db"
username = "azureadmin"
password = "Saihrishi@123"

conn_str = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server=tcp:{server},1433;"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("CONNECTED SUCCESSFULLY")
    conn.close()
except Exception as e:
    print(e)