import  mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pramish"
)

cursor = conn.cursor()
#create object for running sql queries
cursor.execute("CREATE DATABASE IF NOT EXISTS demo")
#executing sql query

print("Database created successfully")

cursor.close()
conn.close()
