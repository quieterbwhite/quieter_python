# -*- coding=utf-8 -*-
# Created Time: 2017年09月29日 星期五 00时10分27秒
# File Name: py_server.py


from py.thrift.generated import PersonService
from PersonServiceImpl import PersonServiceImpl

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

try:
    personServiceHandler = PersonServiceImpl()
    
    processor = PersonService.Processor(personServiceHandler)

    serverSocket = TSocket.TServerSocket(port=8899)
    transportFactory = TTransport.TFramedTransportFactory()
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactory)
    server.serve()
except Thrift.TException, ex:
    print ex.message