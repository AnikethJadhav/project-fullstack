from django.db import models

# Create your models here.


class User(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  gender = models.CharField(max_length=6)
  email = models.EmailField(primary_key=True)

  def __str__(self):
        return self.name
