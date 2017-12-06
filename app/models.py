from django.db import models

class Users(models.Model):
	idUser = models.AutoField(primary_key=True,editable=False)
	mailUser = models.CharField(max_length=45)
	passwordUser = models.CharField(max_length=20)
	active = models.BooleanField(default=False)
	status = models.BooleanField(default=False)
	token_push = models.CharField(max_length=100)
	UserProfile_idUser = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
	Pictures_idUserProfile = models.ForeignKey('Pictures', on_delete=models.CASCADE)
	City_idUser = models.ForeignKey('City', on_delete=models.CASCADE)

class UserProfile(models.Model):
	idUser = models.AutoField(primary_key=True,editable=False)
	nameUserProfile = models.CharField(max_length=20)
	genderUserProfile = models.SmallIntegerField()
	ageUserProfile = models.CharField(max_length=2)
	statusUserProfile = models.CharField(max_length=7, null=True)

class Pictures(models.Model):
	idUserProfile = models.AutoField(primary_key=True,editable=False)
	picture01 = models.CharField(max_length=200,null=True)
	picture02 = models.CharField(max_length=200,null=True)
	picture03 = models.CharField(max_length=200,null=True)

class City(models.Model):
	idUser = models.AutoField(primary_key=True,editable=False)
	default = models.CharField(max_length=40)
	current = models.CharField(max_length=40)
