import pandas as pd
from sqlalchemy import create_engine
import urllib

# Azure SQL credentials
server = "sai-healthtech-server7418.database.windows.net"
database = "healthtech-db"
username = "azureadmin"
password = "YOUR_PASSWORD"

# Connection string
params = urllib.parse.quote_plus(
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server=tcp:{server},1433;"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}",
    fast_executemany=True
)

# Load cleaned dataset
df = pd.read_csv("data/cleaned_healthcare_data.csv")

print("Dataset Shape:", df.shape)

# Upload data
df.to_sql(
    name="patient_readmission",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print("Healthcare dataset uploaded successfully!")