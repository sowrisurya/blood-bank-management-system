# Generated by Django 2.1.2 on 2018-11-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_remove_finalorder_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalorder',
            name='order_complete',
            field=models.BooleanField(default=False),
        ),
    ]