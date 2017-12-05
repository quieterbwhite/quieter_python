# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from kazoo.client import KazooClient

from zoo.zoo_listener import my_listener

from container.service import data_list

def handle_zoo():

    zk = KazooClient(hosts='127.0.0.1:2181')

    zk.start()

    zk.add_listener(my_listener)

    children = zk.get_children("/zookeeper")

    print "There are %s children with names %s" % (len(children), children)

    data_list.extend(children)

    @zk.ChildrenWatch("/zookeeper")
    def watch_children(children):
        print "Children are now: %s" % children

        # 比较当前列表和最新列表的区别，是减少了还是more

        # if less, delete the one

        # if more, add one more, new a client from the value of the new znode

    @zk.DataWatch("/zookeeper")
    def watch_data(data, stat, event):
        """ 在第一次注册的时候，该函数也会被触发

        :param data:
        :param stat:
        :param event:
        :return:
        """

        print "data: %s" % data
        print "stat: %s" % stat.version
        print "event: %s" % event