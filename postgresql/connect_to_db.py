import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,                  # local host name
    user = "root",                        # mysql username
    passwd = "toor"                       # mysql password

)

mycursor = myconnection.cursor()          # my cursor to perform database operations
mycursor.execute("")                      # perform queries on database

# mycursor.execute("SHOW DATABASES")      #to return every database 
# for i in mycursor:
#     print(i)


