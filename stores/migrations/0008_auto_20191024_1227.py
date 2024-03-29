# Generated by Django 2.2.5 on 2019-10-24 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_post_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='code',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='stores.Categorie'),
        ),
    ]
