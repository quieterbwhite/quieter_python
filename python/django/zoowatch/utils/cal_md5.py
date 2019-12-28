# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import types
import hashlib


def md5(content):

    if type(content) is types.StringType:
        m = hashlib.md5()
        m.update(content)
        return m.hexdigest()
    else:
        return ""