# Generated by Django 3.0.1 on 2019-12-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tagline',
            field=models.CharField(default='Lorem ipsum', max_length=200),
        ),
    ]