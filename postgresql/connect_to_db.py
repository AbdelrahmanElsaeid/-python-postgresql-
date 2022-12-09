import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor"

)

mycursor = myconnection.cursor()
mycursor.execute("")

