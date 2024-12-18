from django.db import models
from django.utils.timezone import now

# User Information Model
class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


# Post Model
class Post(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)
    username = models.CharField(max_length=100, default='default username')

    def __str__(self):
        return f'{self.author} - {self.timestamp}'
