import pyodbc

server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'

driver= '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute("SELECT top 10 * from Person.Person")

row = cursor.fetchone()
File=open("person.html", "w")
File.write("<|DOCTYPE html>")
File.write("<html>")
File.write("<body>")
File.write("<h1>First 100 persons in database</h1>")
File.write("<table>")

count=0

while row:
    count+=1
    File.write("<tr><td>" + str(count) + "</td><td>" + row[4] + "</td></tr>")
    row = cursor.fetchone()

File.write("</table>")
File.write("</body>")
File.write("</html>")

File.close()
