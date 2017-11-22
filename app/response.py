from enum import Enum
import simplejson as json

class LoginResponse:
	__token_push = ''
	__user = None

	def __init__(self, token, user):
		self.__token_push = token
		self.__user = user
	def toJSON(self):
		return json.dumps(self.__dict__, cls=ComplexEncoder)

class User:
	__id = 0
	__name = ''
	__email = ''
	__createAt = None
	__updateAt = None

	def __init__(self, id, name, email):
		self.__id = id
		self.__name = name
		self.__email = email
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
	
