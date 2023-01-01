from django.db import models

# Create your models here.
class Ipdata(models.Model):
    ip_address = models.CharField(max_length = 150)
    region = models.CharField(max_length = 150)
    country = models.CharField(max_length = 150)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ip_address