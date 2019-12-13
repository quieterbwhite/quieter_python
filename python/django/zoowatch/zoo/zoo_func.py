# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from kazoo.client import KazooClient

from zoo.zoo_listener import my_listener
from utils.container import data_list

def handle_zoo():

    zk = KazooClient(hosts='127.0.0.1:2181')

    zk.start()

    zk.add_listener(my_listener)

    # List the children
    children = zk.get_children("/zoo")

    print "There are %s children with names %s" % (len(children), children)

    @zk.ChildrenWatch("/zoo")
    def watch_children(children):
        print "Children are now: %s" % children