import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor",
    database = "mydatabase"

)

mycursor = myconnection.cursor()


#mycursor.execute(" SELECT * FROM movies WHERE name ='zelzal' ") 
#mycursor.execute(" SELECT * FROM movies WHERE name LIKE '%Avengers%' ")   # filter by using wildcard
#----------------------Another way ------------------
# sql = " SELECT * FROM movies WHERE name LIKE %s "
# data = ('%Avengers%',)
# mycursor.execute(sql,data)

# result = mycursor.fetchall()                      
# print(result)



#------------------Sort Result in Ascending or descending-------------------------------


# mycursor.execute(" SELECT * FROM movies ORDER BY name ") 
# result = mycursor.fetchall()                      
# print(result)

#------------------Sort in Descending--------------

# mycursor.execute(" SELECT * FROM movies ORDER BY name DESC") 
# result = mycursor.fetchall()                      
# print(result)


#--------------------------Select With Limit------------------------


# mycursor.execute(" SELECT * FROM movies LIMIT 3") 
# result = mycursor.fetchall()                      
# print(result)


#----------------------Limit From  Specific position----------We use OFFSET

mycursor.execute(" SELECT * FROM movies LIMIT 3 OFFSET 2") 
result = mycursor.fetchall()                      
print(result)