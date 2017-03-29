from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User, UserManager

class FriendManager(models.Manager):
    def addFriend(self, user_id, friend_id):
        user = User.objects.get(id=user_id)
        friend = User.objects.get(id=friend_id)
        Friend.objects.create(user=user, friend=friend)
        Friend.objects.create(user=friend, friend=user)
        return {
        'user' : user,
        'friend' : friend
        }

    def removeFriend(self, user_id, friend_id):
        user = User.objects.get(id=user_id)
        friend = User.objects.get(id=friend_id)
        connectionOne = Friend.objects.get(user=user, friend=friend)
        connectionTwo = Friend.objects.get(user=friend, friend=user)
        connectionOne.delete()
        connectionTwo.delete()
        return {
        'user' : user,
        'friend' : friend
        }

class Friend(models.Model):
    user = models.ForeignKey(User, related_name="user_friendship")
    friend = models.ForeignKey(User, related_name="friend_friendship")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FriendManager()
