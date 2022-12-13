import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor",
    database = "mydatabase"

)

mycursor = myconnection.cursor()

mycursor.execute("DELETE FROM movies WHERE name='Shazam' ")


myconnection.commit()