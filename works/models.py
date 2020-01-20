from django.db import models


class Works(models.Model):
    photo = models.ImageField(upload_to='nails_photo')
