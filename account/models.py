from django.db import models

# Create your models here.
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True, default='users/default.png')

    def __str__(self):
        return f'Profile of {self.user.username}'

    @property
    def imageURL(self):
        try:
            url = self.photo.url
            print(url)
        except:
            url = '/users/default.png'
        return url
