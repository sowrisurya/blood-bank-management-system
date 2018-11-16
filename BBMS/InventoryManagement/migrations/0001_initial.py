# Generated by Django 2.1.2 on 2018-11-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('current_inv', models.IntegerField()),
                ('critical', models.CharField(default='NO', max_length=100)),
            ],
        ),
    ]