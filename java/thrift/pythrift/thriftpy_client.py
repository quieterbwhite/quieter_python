# -*- coding=utf-8 -*-

#from py.thrift.generated import PersonService
#from py.thrift.generated import ttypes

"""
基于 eleme thriftpy 实现客户端
"""

import thriftpy
from thriftpy.rpc import make_client

from thriftpy.transport.framed import TFramedTransportFactory
from thriftpy.protocol import TCompactProtocolFactory

pingpong_thrift = thriftpy.load("data.thrift", module_name="data_thrift")

client = make_client(pingpong_thrift.PersonService, '127.0.0.1', 8899,
            proto_factory = TCompactProtocolFactory(),
            trans_factory = TFramedTransportFactory()
        )

person = client.getPersonByUsername("libo")

print person.username
print person.age
print person.married

print '------------'

"""
newPerson = ttypes.Person()
newPerson.username = 'tiger'
newPerson.age = 40
newPerson.married = True

client.savePerson(newPerson)

"""


