from django.db import models


class User(models.Model):
    class Meta:
        db_table = "user"

    username = models.CharField(max_length=32)

    def __str__(self):
        return self.username
