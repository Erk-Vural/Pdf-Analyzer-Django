from django.db import models

from Main.Models.User import User


class Document(models.Model):
    class Meta:
        db_table = "document"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32, blank=True)
    document = models.FileField(upload_to='static/Main/documents/')

    def __str__(self):
        return self.title
