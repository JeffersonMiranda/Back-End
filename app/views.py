from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.models import User
from app.models import Users
from django.http import JsonResponse
from app.response import LoginResponse, User, ComplexEncoder
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
					user = User(users[i].idUser, users[i].nameUser, users[i].mailUser)
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
