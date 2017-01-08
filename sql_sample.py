import pyodbc
#server = 'yourserver.database.windows.net'
server = 'DESKTOP-G8DAE6V'
database = 'AdventureWorks2014'
username = 'sa'
password = 'sa123'
#for mac
#driver = '{/usr/local/lib/libtdsodbc.so}'
#for linux of windows
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("select @@VERSION")
row = cursor.fetchone()
if row:
    print row