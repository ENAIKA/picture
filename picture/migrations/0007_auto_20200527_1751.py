# Generated by Django 3.0.6 on 2020-05-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0006_auto_20200527_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoimage',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='picture.Location'),
        ),
    ]