# Generated by Django 2.0.1 on 2018-02-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180202_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='video_url',
            field=models.URLField(help_text='Add the URL of a video on your YouTube account', null=True, verbose_name='Video URL'),
        ),
    ]
