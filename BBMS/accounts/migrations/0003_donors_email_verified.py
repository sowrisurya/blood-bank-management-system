# Generated by Django 2.1 on 2018-11-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_temp_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='donors',
            name='email_verified',
            field=models.IntegerField(max_length=1, null=True),
        ),
    ]
