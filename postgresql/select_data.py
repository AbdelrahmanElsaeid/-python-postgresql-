import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor",
    database = "mydatabase"

)

mycursor = myconnection.cursor()

#mycursor.execute(" SELECT * FROM movies")
mycursor.execute(" SELECT name FROM movies")       # select column by the name
result = mycursor.fetchall()                      # return all
print(result[2])
# for movie in result:
#     print(movie)

#result = mycursor.fetchone()                       # return first row
#print(result)