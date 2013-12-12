
import sys

from tiddlywebplugins.utils import get_store
from tiddlyweb.config import config


def adduserpolicy(username):
    store = get_store(config)
    bags = store.list_bags()

    for bag in bags:
        bag = store.get(bag)
        read_policy = bag.policy.read

        if username not in read_policy:
            print 'adding %s to %s' % (username, bag.name)
            read_policy.append(username)
        store.put(bag)


if __name__ == '__main__':
    adduserpolicy(sys.argv[1])
