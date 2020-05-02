from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #fullname = models.OneToOneField(User, on_delete=models.CASCADE, blank = True)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    cover = models.ImageField(default="defaultcover.jpg", upload_to="cover_pics")
    about = models.CharField(max_length=250, blank = True)
    linkedin = models.CharField(max_length=250, blank = True)
    github = models.CharField(max_length=250, blank = True)
    twitter = models.CharField(max_length=250, blank = True)
    instagram = models.CharField(max_length=250, blank = True)

    def __str__(self):
        return f"{self.user.username} Profile"


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
