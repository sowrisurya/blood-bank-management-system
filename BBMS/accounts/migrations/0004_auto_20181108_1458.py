# Generated by Django 2.1 on 2018-11-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_donors_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='email_verified',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='email_verified',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='donors',
            name='email_verified',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='temp_db',
            name='code',
            field=models.IntegerField(),
        ),
    ]