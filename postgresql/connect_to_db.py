import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor"

)

mycursor = myconnection.cursor()
mycursor.execute("")

# mycursor.execute("SHOW DATABASES")    #to return every database 
# for i in mycursor:
#     print(i)


