#!C:\Users\Ishubrowung\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi

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
if __name__ == "__main__":
    try:
        htmlTop()
        htmlTail()
    except:
        cgi.print_exception()

x = 5
