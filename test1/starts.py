"""
Select filter: select=starts:1
"""

from tiddlyweb.filters.select import ATTRIBUTE_SELECTOR


def starts(entity, attribute, value):
    try:
        return entity.name.startswith(value)
    except AttributeError:
        return entity.title.startswith(value)

def init(config):
    ATTRIBUTE_SELECTOR['starts'] = starts


