# Generated by Django 3.0.6 on 2020-05-25 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoimage',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='photoimage',
            name='location',
            field=models.ManyToManyField(to='picture.Location'),
        ),
    ]