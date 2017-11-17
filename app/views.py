from django.shortcuts import render

users = Users.objects.all()

def login(request):
	return render(request,'app/login.html')
