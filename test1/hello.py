
from tiddlywebplugins.templates import get_template

def hello(environ, start_response):

    username = environ['tiddlyweb.usersign']['name']
    template = get_template(environ, 'hello.html')
            
    start_response('200 OK', [
        ('Content-Type', 'text/html')])
    return template.render({'username': username})

def init(config):
    config['selector'].add('/extras/hello', GET=hello)


