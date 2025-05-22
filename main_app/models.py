from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.artist}'

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    song_owner = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')

    def __str__(self):
        return self.title


