import sqlite3

def connect(dbname):
    connection=sqlite3.connect(dbname)
    connection.execute("CREATE TABLE IF NOT EXISTS HOTEL (NAME TEXT, ADDRESS TEXT, PRICE TEXT, AMENITIES TEXT,RATING TEXT)")
    print("The table was created successfully")
    connection.close()

def insert(dbname,values):
    connection=sqlite3.connect(dbname)
    connection.execute("INSERT INTO HOTEL (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES(?, ?, ?, ?, ?)",values)
    connection.commit()
    connection.close()

def hotel_info(dbname):
    connection=sqlite3.connect(dbname)
    curr=connection.cursor()
    curr.execute("SELECT * FROM HOTEL")
    data=curr.fetchall()
    for i in data:
        print(i)
    connection.close()

