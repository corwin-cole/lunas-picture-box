# Generated by Django 2.0.1 on 2018-02-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180202_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='link_text',
            field=models.CharField(help_text='Clickable text', max_length=200),
        ),
    ]
