# Generated by Django 4.2 on 2023-06-28 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(to='blog_app.categoria', validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]
