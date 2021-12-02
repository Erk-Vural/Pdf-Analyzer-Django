from django.db import models


# Create your models here.

class Admin(models.Model):
    class Meta:
        db_table = "admin"

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class User(models.Model):
    class Meta:
        db_table = "user"

    username = models.CharField(max_length=32)

    def __str__(self):
        return self.username

