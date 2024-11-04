import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=45.127.108.208,5863;"
    "DATABASE=PssDataExport;"
    "UID=sa;"
    "PWD=RPSsql12345;"
)

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print('Connected to the database Successfully.')

    try:
        cursor.execute("ALTER TABLE Devices ADD new_column VARCHAR(255);")
        conn.commit()
        print('Column added sucessfuly.')
    except Exception as e:
        print(f'Error Executing Alter Statemet: {e}')
except Exception as e:
    print(f'failed to Connect to Database: {e}')
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print('Connection Closed.')