import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor",
    database = "mydatabase"

)

mycursor = myconnection.cursor()

#mycursor.execute(" SELECT * FROM movies")
#mycursor.execute("ALTER TABLE movies ADD COLUMN language VARCHAR(40) ")         # add  new column     
# mycursor.execute("ALTER TABLE movies CHANGE language language VARCHAR(70) ")     # update type of column

#mycursor.execute(" UPDATE movies SET plot = 'using the update' WHERE name = 'zelzal' ") # update value

# ---------------------------Another Way--------------------------
sql = " UPDATE movies SET plot = %s WHERE name = %s "
data = ('a good horror movie', 'Now You See Me')
mycursor.execute(sql, data)

myconnection.commit()