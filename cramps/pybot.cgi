#!C:\Users\Ishubrowung\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi

def getData():
    formData = cgi.FieldStorage()
    text = formData.getvalue('names')
    return text

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

   

#main program
htmlTop()
stuff = getData()
htmlTail()
print("Hey {0}...".format(stuff))
