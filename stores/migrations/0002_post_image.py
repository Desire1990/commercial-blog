# Generated by Django 2.2.6 on 2019-10-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default=0, max_length=2083),
        ),
    ]
