# Generated by Django 3.1.7 on 2021-02-27 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('Permitted', models.BooleanField(default=False)),
                ('Students_acc_male', models.IntegerField(default=0)),
                ('Students_acc_female', models.IntegerField(default=0)),
                ('Students_accd_male', models.IntegerField(default=0)),
                ('Students_accd_female', models.IntegerField(default=0)),
                ('Guest_acc', models.IntegerField(default=0)),
                ('Guest_accd', models.IntegerField(default=0)),
                ('Organised', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.organiser')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Femaleness', models.BooleanField()),
                ('Mobile', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Come_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organiser.event')),
            ],
        ),
    ]
