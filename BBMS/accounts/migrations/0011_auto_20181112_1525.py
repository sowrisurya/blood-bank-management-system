# Generated by Django 2.1 on 2018-11-12 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20181111_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_line1', models.CharField(max_length=150)),
                ('ad_line2', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'T')], max_length=1)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('blood_group', models.CharField(choices=[('O_pos', 'O+'), ('O_neg', 'O-'), ('A_pos', 'A+'), ('A_neg', 'A-'), ('B_pos', 'B+'), ('B_neg', 'B-'), ('AB_pos', 'AB+'), ('AB_neg', 'AB-')], max_length=3)),
                ('d_o_b', models.DateField()),
                ('ph_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Donor_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('las_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('hospital_name', models.CharField(max_length=100)),
                ('ad_line1', models.CharField(max_length=150)),
                ('ad_line2', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=20)),
                ('license', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'T')], max_length=1)),
                ('blood_group', models.CharField(choices=[('O_pos', 'O+'), ('O_neg', 'O-'), ('A_pos', 'A+'), ('A_neg', 'A-'), ('B_pos', 'B+'), ('B_neg', 'B-'), ('AB_pos', 'AB+'), ('AB_neg', 'AB-')], max_length=3)),
                ('d_o_b', models.DateField()),
                ('ph_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='donors',
        ),
        migrations.DeleteModel(
            name='hospital',
        ),
        migrations.DeleteModel(
            name='users',
        ),
        migrations.AddField(
            model_name='patient_details',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Patient_reg'),
        ),
        migrations.AddField(
            model_name='donor_details',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Donor_reg'),
        ),
    ]
