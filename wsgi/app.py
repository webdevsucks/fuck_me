#!C:\Users\Ishubrowung\AppData\Local\Programs\Python\Python35-32 python

import cgi
from cgi import parse_qs, escape
from paste import request
def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'
    if environ["REQUEST_METHOD"] == "POST":
        s = 3
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        form = cgi.FieldStorage(fp=environ['wsgi.input'],environ=post_env,keep_blank_values=True)
        #output = b''+form["word"].value
        #output = form.getvalue('word')
        #output = str.encode(output) 
        content_length = int(environ['CONTENT_LENGTH'])
        output = environ['wsgi.input'].read(content_length)
        fields = request.parse_formvars(environ)
        field = fields['word']
##        output = str.encode(fields)
        #temp = parse_qs(output)
        #temp = parse_qs(environ['QUERY_STRING'])
        #output = temp.get('word',[''])[0]
        #output = str.encode(output)
        #output = output.word.value #can't get it to work with forms :/
        #print(b'bloop')
##    #form = cgi.FieldStorage()
##    #q = form.getvalue('q')
##
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
	
if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('localhost', 8080, app)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
