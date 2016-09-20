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

def getPeople(db,conn):
    sql = "select * from person"
    cursor.execute(sql)
    people = cursor.fetchall()
    return people

def createDropDown(people):
    #set up drop down menu
    print("""<select name="drop">""")
    for person in people:
        print("""<option value={0}">{1} {2}</option>""".format(person[0],person[1],person[2]))
    print("</select><br>")

def createForm(people):
    print("""<form method="post" action="process.cgi">""")
    createDropDown(people)
    print("""<input type="submit" name="submit" value="Submit">""")
    print("</form>")

def createRadioButtons(people):
    #set up radio buttons
    for person in people:
        print("""<input type="radio" name="radio" value={0}">{1} {2}""".format(person[0],person[1],person[2]))
    print("<br>")


def createCheckBoxes(people):
    #set up radio buttons
    for person in people:
        print("""<input type="checkbox" name="check" value={0}">{1} {2}""".format(person[0],person[1],person[2]))
    print("<br>") 

#main program
htmlTop()
db, cursor = connectDB()
people = getPeople(db, cursor)
cursor.close()
createForm(people)
createRadioButtons(people)
createCheckBoxes(people)
htmlTail()
