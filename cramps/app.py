import cgi

def application(environ, start_response):
    status = '200 OK'
	form = cgi.FieldStorage()
	q = form.getvalue('q')
    output = b(q)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]