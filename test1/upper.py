
from tiddlyweb.serializations.html import Serialization as HTMLSerialization

class Serialization(HTMLSerialization):

    def tiddler_as(self, tiddler):
        tiddler.text = tiddler.text.upper()
        return HTMLSerialization.tiddler_as(self, tiddler)

def init(config):
    config['extension_types']['up'] = 'text/rhtml'
    config['serializers']['text/rhtml'] = ['upper', 'text/html; charset=UTF-8']
