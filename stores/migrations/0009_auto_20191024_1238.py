# Generated by Django 2.2.5 on 2019-10-24 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0008_auto_20191024_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Categorie'),
        ),
        migrations.AlterField(
            model_name='post',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='stock',
            field=models.IntegerField(),
        ),
    ]