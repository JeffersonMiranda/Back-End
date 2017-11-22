from django.db import models

class Users(models.Model):
	idUser = models.AutoField(primary_key=True,editable=False)
	nameUser = models.CharField(max_length=20, default='thallyssonklein')
	mailUser = models.CharField(max_length=45)
	passwordUser = models.CharField(max_length=20)
	createdAt = models.DateTimeField()
	updateAt = models.DateTimeField()
	active = models.BooleanField(default=False)
	status = models.BooleanField(default=False)
	token_push = models.CharField(max_length=100)
