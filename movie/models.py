from django.db import models

# Create your models here.

class Movies(models.Model):

    name = models.CharField(max_length=99)
    img = models.ImageField(upload_to='pictures')
    
    