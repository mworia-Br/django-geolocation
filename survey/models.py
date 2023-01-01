from django.db import models

# Create your models here.

class Data(models.Model):
    location = models.CharField(max_length=255, null=True)
    mobile_phone = models.CharField(max_length=15, null=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name