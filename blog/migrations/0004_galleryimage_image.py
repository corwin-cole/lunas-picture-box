# Generated by Django 2.0.1 on 2018-02-02 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20180202_0458'),
        ('blog', '0003_auto_20180202_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Photo'),
        ),
    ]
