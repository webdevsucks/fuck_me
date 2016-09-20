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

def selectPeople(db, cursor):
    sql = "select * from person"
    cursor.execute(sql)
    #fetch results
    people = cursor.fetchall()
    return people

def displayPeople(people):
    print("<table border ='1'>")
    print("<tr>")
    print("<th>ID</th>")
    print("<th>First Name</th>")
    print("<th>Last Name</th>")
    print("</tr>")
    for each in people:
        print("<tr>")
        print("<td>{0}</td>".format(each[0]))
        print("<td>{0}</td>".format(each[1]))
        print("<td>{0}</td>".format(each[2]))
        print("</tr>")
    print("</table>")

#main program
htmlTop()
db, cursor = connectDB()
people = selectPeople(db, cursor)
cursor.close()
displayPeople(people)
htmlTail()
