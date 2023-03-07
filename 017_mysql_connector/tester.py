import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='sakila'
)
conn.autocommit = True
mycursor = conn.cursor()

mycursor.execute('SELECT * FROM actor')

result = mycursor.fetchmany(5)
print(result)
