
import sys

from tiddlywebplugins.utils import get_store
from tiddlyweb.config import config


def fixbags():
    store = get_store(config)
    bags = store.list_bags()

    for bag in bags:
        bag = store.get(bag)
        bag.policy.read = []
        store.put(bag)


if __name__ == '__main__':
    fixbags()
