# Generated by Django 2.2.3 on 2019-09-08 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BujaMovies', '0003_achats_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achats',
            name='slug',
            field=models.ForeignKey(default=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='BujaMovies.Films'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='films',
            name='cover',
            field=models.ImageField(null=True, upload_to='Covers/'),
        ),
        migrations.AlterField(
            model_name='films',
            name='film',
            field=models.FileField(null=True, upload_to='Videos/'),
        ),
        migrations.AlterField(
            model_name='films',
            name='prix_telechargement',
            field=models.FloatField(help_text='BIF', verbose_name='Prix de Téléchargement'),
        ),
    ]