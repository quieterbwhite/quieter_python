# -*- coding=utf-8 -*-
# Created Time: 2017年09月28日 星期四 23时59分19秒
# File Name: PersonServiceImpl.py

from py.thrift.generated import ttypes

class PersonServiceImpl(object):

    def getPersonByUsername(self, username):
        print "Got client param: " + username

        person = ttypes.Person()
        person.username = 'libo'
        person.age = 10
        person.married = True

        return person

    def savePerson(self, person):

        print "Got client param: "

        print person.username
        print person.age
        print person.married
