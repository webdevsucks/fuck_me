#!C:\Users\Ishubrowung\AppData\Local\Programs\Python\Python35-32\python.exe
#!C:\Program Files\MySQL\bin

import cgi

import pymysql as conn

def htmlTop():
    print("""Content-type:text/html\n\n
            <DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="utf-8"/>
            <title>server-side template</title>
            </head>
            <body>""")

def htmlTail():
    print("""</body>
        </html>""")


def connectDB():
    db = conn.connect(host='localhost', user='root', passwd='jennyxj9')
    cursor = db.cursor()
    return db, cursor

def createDB(db, cursor):
    #create a new database
    sql = "create database example"
    cursor.execute(sql)
    db.commit()

def createEntity(db, cursor):
    #use the newly created database
    sql = "use example"
    cursor.execute(sql)
    #create a simple entity
    sql = '''create table person
             (personid int not null auto_increment,
             firstName varchar(20) not null,
             lastName varchar(30) not null,
             primary key(personid))'''
    cursor.execute(sql)
    db.commit()

#main program
htmlTop()
db,cursor = connectDB()
createDB(db,cursor)
createEntity(db,cursor)
#close the connection
cursor.close()
htmlTail()
