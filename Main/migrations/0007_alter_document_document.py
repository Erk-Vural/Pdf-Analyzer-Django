# Generated by Django 3.2.9 on 2021-12-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_alter_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
