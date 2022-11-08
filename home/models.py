from django.db import models

# Create your models here.
class wishes(models.Model):
  name=models.CharField(max_length=50)
  message=models.TextField()
  image=models.ImageField(default="default/default.png")
  