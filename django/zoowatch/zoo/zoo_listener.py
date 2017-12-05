# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from logs.mylog import flogger

from kazoo.client import KazooState

def my_listener(state):
    if state == KazooState.LOST:
        # Register somewhere that the session was lost
        flogger.info("KazooState.LOST")
    elif state == KazooState.SUSPENDED:
        # Handle being disconnected from Zookeeper
        flogger.info("KazooState.SUSPENDED")
    else:
        # Handle being connected/reconnected to Zookeeper
        flogger.info("KazooState UNKNOWN")
