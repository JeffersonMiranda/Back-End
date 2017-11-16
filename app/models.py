from django.db import models

class Users(models.Model):
	idUser = models.UUIDField(primary_key=True, editable=False)
	mailUser = models.CharField(max_length=45)
	passwordUser = models.CharField(max_length=20)
	createAt = models.DateTimeField()
	updateAt = models.DateTimeField()
	active = models.BooleanField(default=False)
	status = models.BooleanField(default=False)
