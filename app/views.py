from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.models import User
from app.models import Users, UserProfile, Pictures, City
from django.http import JsonResponse
from app.response import LoginResponse, User, Sex, City, Photos
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
					user = User(users[i].idUser, userProfile.nameUserProfile, users[i].mailUser, userProfile.ageUserProfile, userProfile.genderUserProfile, City(city.default,city.current), users[i].createdAt, users[i].updatedAt, Photos(pictures.picture01,pictures.picture02,pictures.picture03))
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
	i = 0
	userObj = Users(mailUser=email,nameUser=name,passwordUser=password,token_push=token_push)
	userObj.save()
	user = User(userObj.idUser, userObj.nameUser, userObj.mailUser)
	loginResponse = LoginResponse(token_push, user)
	return JsonResponse(loginResponse.getDict())
