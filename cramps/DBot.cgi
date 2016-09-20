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
    db = conn.connect(host='localhost',user='root',passwd='jennyxj9',db='example')
    cursor = db.cursor()
    return db, cursor

def createPersonList():
    #create people list
    people = []
    #add people
    people.append(["Adam","McNiel"])
    people.append(["Jerry","Springer"])
    people.append(["Rope","Safe"])
    people.append(["Sax","Phone"])
    people.append(["Lock","Jaw"])
    return people

def insertPeople(db, cursor, people):
    for each in people:
        sql = "insert into person(firstName, lastName) values('{0}','{1}')".format(each[0],each[1])
        cursor.execute(sql)
    db.commit()

#main program
htmlTop()
db, cursor = connectDB()
people = createPersonList()
insertPeople(db, cursor, people)
htmlTail()

    
