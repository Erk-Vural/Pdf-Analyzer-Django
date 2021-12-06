from django.db import models

from Main.Models.Document import Document
from Main.Models.User import User


class Author(models.Model):
    class Meta:
        db_table = "Author"

    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Document, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    student_number = models.CharField(max_length=32)
    education_type = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.last_name