from enum import Enum
import simplejson as json

class LoginResponse:
	__token_push = ''
	__user = None

	def __init__(self, token, user):
		self.__token_push = token
		self.__user = user

	def getUserDict(self):
		return dict((('id',self.getUser().getId()),
('name',self.getUser().getName()),('email',self.getUser().getEmail()),('age',self.getUser().getAge()),('gender',self.getUser().getGender())
,('city',self.getCityDict()),('photos',self.getPhotosDict())))

	def getCityDict(self):
		return dict((('default',self.getUser().getCity().getDefault()),('current',self.getUser().getCity().getCurrent())))

	def getPhotosDict(self):
		return dict((('photo1',self.getUser().getPhotos().getPhoto1()),('photo2',self.getUser().getPhotos().getPhoto2()),('photo3',self.getUser().getPhotos().getPhoto3())))

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
	__age = 0
	__gender = None
	__city = None
	__photos = None

	def __init__(self, id, name, email, age, gender, city, photos):
		self.__id = id
		self.__name = name
		self.__email = email
		self.__age = age
		self.__gender = gender
		self.__city = city
		self.__createdAt = createdAt
		self.__updatedAt = updatedAt
		self.__photos = photos

	def getId(self):
		return self.__id

	def getName(self):
		return self.__name

	def getEmail(self):
		return self.__email	

	def getAge(self):
		return self.__age

	def getCity(self):
		return self.__city

	def getCreatedAt(self):
		return self.__createdAt

	def getUpdatedAt(self):
		return self.__updatedAt

	def getPhotos(self):
		return self.__photos

	def getGender(self):
		return self.__gender

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

	def getDefault(self):
		return self.__default

	def getCurrent(self):
		return self.__current

class Photos:
	__photo1 = None
	__photo2 = None
	__photo3 = None

	def __init__(self, photo1, photo2, photo3):
		self.__photo1 = photo1
		self.__photo2 = photo2
		self.__photo3 = photo3

	def getPhoto1(self):
		return self.__photo1

	def getPhoto2(self):
		return self.__photo2

	def getPhoto3(self):
		return self.__photo3
