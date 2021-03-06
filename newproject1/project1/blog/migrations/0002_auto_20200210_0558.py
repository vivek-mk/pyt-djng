# Generated by Django 2.2.9 on 2020-02-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
