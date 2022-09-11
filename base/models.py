from django.db import models
from django.contrib.auth.models import User # django provides their own user model

# Create your models here.

# CLass we create represents the Database Table, every attribute in the class is a column and class instance is a row

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model): 
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200) # required paramater for this value
    description = models.TextField(null=True, blank=True) # by default null is set to false, null is allowed with true means it can be blank, from can also be empty with blank true
    #participants = 
    updated = models.DateTimeField(auto_now=True) # every time the save method is called take a time stamp
    created = models.DateTimeField(auto_now_add=True) # only saved when we first create the instance so if we save it multiple times it wont change it

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
            return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user can have many messages, message can only have one user.
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # when the parent is deleted, all the children also get deleted
    body = models.TextField() # force user to write message
    updated = models.DateTimeField(auto_now=True) # every time the save method is called take a time stamp
    created = models.DateTimeField(auto_now_add=True) # only saved when we first create the instance so if we save it multiple times it wont change it

    def __str__(self):
            return self.body[0:50] # slide type of thing
