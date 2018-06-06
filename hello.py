def app (environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type','text/plain')]
	start_response(status, response_headers)
	resp = environ['QUERY_STRING'].split("&")
	resp = [item+"\r\n" for item in resp]
	return resp
# ===================================
#def app(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
#                  encoding="utf8")]
# ===================================
# ===================================

#def app(environ, start_response):
#    """Simplest possible application object"""
#    data = environ['QUERY_STRING'].split('&')
#    data = [item+'\r\n' for item in data]
#    data = [item.encode() for item in data]
#    status = '200 OK'
#    response_headers = [
#        ('Content-type','text/plain'),
#    ]
#    start_response(status, response_headers)
#    return iter(data)