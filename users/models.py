from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from maths.models import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    math_id = models.ForeignKey(Maths, null=True, on_delete = models.CASCADE)
    # business_id = models.ForeignKey(Business, null=True, on_delete = models.CASCADE)
    # role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Resident', 'Resident')], default='Resident')

    def __str__(self):
        return f'{self.user} Profile'



    # overriding save and resizing then saving
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)