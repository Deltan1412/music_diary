from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    song_owner = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')

    def __str__(self):
        return self.title


