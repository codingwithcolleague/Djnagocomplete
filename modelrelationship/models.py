from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=200)
    page_cat = models.CharField(max_length=100)
    page_publish = models.DateField(null=True,blank=True)


class Like(Page):
    likes = models.IntegerField()

class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    post_title = models.CharField(max_length=200)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()

"""
Many to Many Relation ship
"""


class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def written_by(self):
        return ",".join([ str(i) for i in self.user.all()])