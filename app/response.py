from enum import Enum
import simplejson as json

class LoginResponse:
	__token_push = ''
	__user = None

	def __init__(self, token, user):
		self.__token_push = token
		self.__user = user

	def getUserDict(self):
		return dict((('id',self.getUser().getId()),('name',self.getUser().getName()),('email',self.getUser().getEmail())))

	def getDict(self):
		return dict((('token_push',self.getToken()),('user', self.getUserDict())))

	def getToken(self):
		return self.__token_push

	def getUser(self):
		return self.__user

	def toJSON(self):
		return json.dumps(self.__dict__, cls=ComplexEncoder)

class User:
	__id = 0
	__name = ''
	__email = ''

	def __init__(self, id, name, email):
		self.__id = id
		self.__name = name
		self.__email = email
	
	def getId(self):
		return self.__id

	def getName(self):
		return self.__name

	def getEmail(self):
		return self.__email

	def toJSON(self):
		return json.dumps(self.__dict__,cls=ComplexEncoder)

class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, LoginResponse) or isinstance(obj, User):
			return obj.toJSON()
		else:
			return json.JSONEncoder.default(self, obj)

class Sex(Enum):
	FAMALE = 2
	MALE = 4
	UNDEFINED = 8

class City:
	__default = ''
	__current = ''

	def __init__(self, default, current):
		self.__default = default
		self.__current = current
	
