from django.db import models
from django.contrib.auth.models import User

class User_Login(models.Model):
    name=models.CharField(max_length=50)
    coins=models.IntegerField(default=5000)
    tournament=models.TextField()

    def __str__(self):
        return self.name
    
class GameRecord(models.Model):
    name=models.CharField(max_length=50)
    guess=models.IntegerField()
    attempt=models.IntegerField(default=0)
    status=models.CharField(max_length=50)
    score=models.IntegerField()

    def __str__(self):
        return self.name

class GameHistory(models.Model):
    name=models.CharField(max_length=50)
    input=models.IntegerField()
    key = models.CharField(max_length=4)

    attempt=models.IntegerField(default=0)
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Tournament(models.Model):
    name=models.TextField()
    price=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
class TounamentHistory(models.Model):
    username=models.CharField(max_length=255 )
    name=models.TextField()
    price=models.IntegerField()
    date=models.DateField()

    def __str__ (self):
        return self.name
    



