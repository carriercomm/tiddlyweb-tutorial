
from tiddlywebplugins.templates import get_template
from tiddlyweb.web.util import tiddler_url

from tiddlyweb.model.bag import Bag
from tiddlyweb.model.tiddler import Tiddler


def hello(environ, start_response):
    store = environ['tiddlyweb.store']
    username = environ['tiddlyweb.usersign']['name']
    template = get_template(environ, 'hello.html')

    tiddlers = store.list_bag_tiddlers(Bag('system'))
    bags = [store.get(bag) for bag in store.list_bags()]
            
    start_response('200 OK', [
        ('Content-Type', 'text/html')])
    return template.render({'username': username,
        'tiddlers': tiddlers,
        'bags': bags,
    })


def create(environ, start_response):
    store = environ['tiddlyweb.store']
    username = environ['tiddlyweb.usersign']['name']

    query = environ['tiddlyweb.query']

    title = query['title'][0]
    text = query['text'][0]

    tiddler = Tiddler(title, 'common')
    tiddler.text = text
    tiddler.modifier = username
    store.put(tiddler)

    start_response('303 Found', [
        ('Location', tiddler_url(environ, tiddler))])
    return []

def init(config):
    config['selector'].add('/extras/hello', GET=hello)
    config['selector'].add('/extras/create', POST=create)


