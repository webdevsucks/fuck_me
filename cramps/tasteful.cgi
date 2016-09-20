#!C:\Users\Ishubrowung\AppData\Local\Programs\Python\Python35-32\python.exe
#!C:\Program Files\MySQL\bin

import cgi
import os
import cgitb; cgitb.enable()  # for troubleshooting

form = cgi.FieldStorage()
q = form.getvalue('q')
print ("Content-Type: text/html\n") 
print (q)
