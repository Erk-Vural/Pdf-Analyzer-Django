from django.db import models

from Main.Models.Document import Document
from Main.Models.User import User


class MentorInfo(models.Model):
    class Meta:
        db_table = "MentorInfo"

    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Document, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.last_name