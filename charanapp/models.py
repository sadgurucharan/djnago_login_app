from django.db import models

class email_data(models.Model):
    email=models.CharField(max_length=255,primary_key=True)
    password=models.CharField(max_length=255)

# Create your models here.
