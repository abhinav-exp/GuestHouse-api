# Generated by Django 3.1.7 on 2021-02-27 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organiser', '0008_auto_20210227_1149'),
        ('Public', '0002_remove_student_come_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('Femaleness', models.BooleanField()),
                ('Mobile', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Attending', models.ManyToManyField(to='Organiser.Event')),
            ],
        ),
    ]
