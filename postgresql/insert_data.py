import mysql.connector 

myconnection = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "toor",
    database = "mydatabase"

)

mycursor = myconnection.cursor()

# sql = "INSERT INTO movies(name, plot) VALUES(%s , %s)"
# data = ("Avengers End Game", 'Fight movie')

# mycursor.execute(sql, data)
# myconnection.commit()
# print("Data is inserted ")

#  -----------------Insert Multiple Rows--------------------

sql = "INSERT INTO movies(name, plot) VALUES(%s , %s)"
data = [("Now You See Me ", "story of some wizards"),
        ("Avengers ", "story of some super heros"),
        ("Shazam ", "story of some super shazam"),
        
        ]

mycursor.executemany(sql, data)
myconnection.commit()
print("Data is inserted ")
