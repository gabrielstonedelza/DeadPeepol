# Generated by Django 3.0.3 on 2020-02-20 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vtrack',
            old_name='user_platform',
            new_name='user_album',
        ),
    ]
