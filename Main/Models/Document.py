from django.db import models

from Main.Models.User import User


class Document(models.Model):
    class Meta:
        db_table = "document"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='static/Main/documents/')

    def __str__(self):
        return self.document


class Author(models.Model):
    class Meta:
        db_table = "Author"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    student_number = models.CharField(max_length=32)
    education_type = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.last_name


class CourseName(models.Model):
    class Meta:
        db_table = "CourseName"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content


class Summary(models.Model):
    class Meta:
        db_table = "Summary"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)

    def __str__(self):
        return self.content


class Semester(models.Model):
    class Meta:
        db_table = "Semester"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content


class Title(models.Model):
    class Meta:
        db_table = "Title"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content


class Keyword(models.Model):
    class Meta:
        db_table = "Keywords"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.content


class MentorInfo(models.Model):
    class Meta:
        db_table = "MentorInfo"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.last_name


class JuryInfo(models.Model):
    class Meta:
        db_table = "JuryInfo"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.last_name
