import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor",
    database = "mydatabase"

)

mycursor = myconnection.cursor()
mycursor.execute("CREATE TABLE movies (name VARCHAR(100) , plot VARCHAR(500))")
print("Created Success")

