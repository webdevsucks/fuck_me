#!C:\Users\Ishubrowung\AppData\Local\Programs\Python\Python35-32\python.exe
#!C:\pip\pypyodbc

import cgi

import sys
sys.path.append('C:\pip\pypyodbc')
import pypyodbc



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

x = 5
y = x * x

#main program
if __name__ == "__main__":
    try:
        htmlTop()
        htmlTail()
        print(y)
    except:
        cgi.print_exception()


