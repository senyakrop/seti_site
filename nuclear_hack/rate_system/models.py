from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Utype(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, db_index=True, verbose_name="Type")
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('type', kwargs={'type_slug': self.slug})

class Criterions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mark = models.IntegerField(null=True, blank=True, verbose_name="Mark")
    upload = models.FileField(upload_to='uploads/', verbose_name="Upload")
    characteristic = models.CharField(max_length=250, verbose_name="Characteristic", null=True, blank=True)
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('description', kwargs={'description_slug': self.slug})