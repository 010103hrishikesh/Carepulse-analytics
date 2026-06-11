import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:sai-healthtech-server7418.database.windows.net,1433;"
    "Database=healthtech-db;"
    "Uid=azureadmin;"
    "Pwd=Saihrishi@123;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM patient_readmission")

print("Rows in table:", cursor.fetchone()[0])

conn.close()