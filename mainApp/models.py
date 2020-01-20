from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='services_photo')

    def __str__(self):
        return self.title
