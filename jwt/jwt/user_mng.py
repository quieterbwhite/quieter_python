# -*- coding=utf-8 -*-

'''
user manager
'''

from jwt.models import JWTUser

class UserManager(object):
	''' 用户管理 '''

	def __init__(self, uid):
		self.user = JWTUser.objects(id=uid).first()

	@classmethod
	def save_user(self, u):
		user = JWTUser.create_user(
				username = u['username'],
				password = u['password']
			)
		user.mobile = u['mobile']
		user.email = u['email']
		user.save()

	@classmethod
	def find_user(self, username=None, mobile=None):	
		query = {}
		if username: query.update('username':username)
		if mobile:   query.update('mobile':mobile)
		return JWTUser.objects(__raw__=query)
