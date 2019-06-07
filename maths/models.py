from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Maths(models.Model):
    topic = models.CharField(max_length = 100)
    sub_topic = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/', default = 'default.jpg')
    description = models.TextField(default = 'No description')
    grade = models.IntegerField(default = '0')
    instructor = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic

    def create_maths(self):
        self.save()

    def delete_maths(self):
        self.delete()

    def find_maths(hoods_id):
        maths = Maths.objects.get(id = maths_id)
        return maths

    def update_maths(self, item, value):
        self.update(item = value)