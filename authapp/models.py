from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=24)

    def __str__(self):
        return self.email
