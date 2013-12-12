"""
Lower case content put to bags when no tiddler.type

NOTE: Accept constraint must be set to something other than []
(e.g. "NONE") to get validators to run.
"""

from tiddlyweb.web.validator import TIDDLER_VALIDATORS

def lowerit(tiddler, environ):

    print 'lower it seen with', tiddler.title
    if tiddler.type:
        return

    tiddler.text = tiddler.text.lower()

def init(config):
    TIDDLER_VALIDATORS.append(lowerit)

