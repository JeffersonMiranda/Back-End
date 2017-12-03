from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.models import User
from app.models import Users, UserProfile, Pictures, City
from django.http import JsonResponse
from app.response import LoginResponse, User, Sex, City as CityResponse, Photos
import json

@csrf_exempt
def login(request):
	users = Users.objects.all()
	email = request.POST.get('email')
	password = request.POST.get('password')
	token_push = request.POST.get('token_push')
	i = 0
	for user in users:
		if users[i].mailUser == email:
			if users[i].passwordUser == password:
				if users[i].token_push == token_push:
					userProfile = UserProfile.objects.filter(idUser=users[i].UserProfile_userId)
					pictures = Pictures.objects.filter(idUserProfile=users[i].Pictures_idUserProfile)
					city = City.objects.filter(idUser=users[i].City_idUser)
					user = User(users[i].idUser, userProfile.nameUserProfile, users[i].mailUser, userProfile.ageUserProfile, userProfile.genderUserProfile, City(city.default,city.current), Photos(pictures.picture01,pictures.picture02,pictures.picture03))
					loginResponse = LoginResponse(token_push, user)
					return JsonResponse(loginResponse.getDict())
		++i
	return HttpResponse('No sucess')

@csrf_exempt
def sign(request):
	users = Users.objects.all()
	email = request.POST.get('email')
	name = request.POST.get('name')
	password = request.POST.get('password')
	token_push = request.POST.get('token_push')
	age = request.POST.get('age')
	gender = request.POST.get('gender')
	defaultCity = request.POST.get('defaultCity')
	currentCity = request.POST.get('currentCity')
	photo1 = request.POST.get('photo1')
	photo2 = request.POST.get('photo2')
	photo3 = request.POST.get('photo3')
	i = 0
	userProfileObj = UserProfile(nameUserProfile=name,genderUserProfile=gender,ageUserProfile=age)
	cityObj = City(default=defaultCity,current=currentCity)
	picturesObj = Pictures(picture01=photo1,picture02=photo2,picture03=photo3)
	userObj = Users(mailUser=email,passwordUser=password,token_push=token_push,UserProfile_idUser=userProfileObj.idUser,City_idUser=cityObj.idUser,Pictures_idUserProfile=picturesObj.idUserProfile)
	userObj.save()
	user = User(userObj.idUser, userObj.nameUser, userObj.mailUser, userProfileObj.ageUserProfile, userProfileObj.genderUserProfile, CityResponse(cityObj.default, cityObj.current), Photos(photo1,photo2,photo3))
	loginResponse = LoginResponse(token_push, user)
	return JsonResponse(loginResponse.getDict())
