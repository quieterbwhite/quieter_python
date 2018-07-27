# -*- coding: utf-8 -*-

import simplejson

def dumps_ident(data, indent=4, separators=(',', ':')):

    return simplejson.dumps(data, indent=indent, separators=separators)