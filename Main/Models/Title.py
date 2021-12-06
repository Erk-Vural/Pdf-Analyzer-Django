from django.db import models

from Main.Models.Document import Document
from Main.Models.User import User


class Title(models.Model):
    class Meta:
        db_table = "Title"

    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Document, null=True, on_delete=models.CASCADE)

    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content