# Generated by Django 4.0.1 on 2022-01-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0022_alter_message_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]