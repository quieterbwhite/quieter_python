# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json


def dumps_ident(data, indent=4, separators=(',', ':')):

    return json.dumps(data, indent=indent, separators=separators)
