# Generated by Django 2.2.7 on 2019-11-27 10:51

from django.db import migrations, models
import django_countries.fields
import django_mysql.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('usernameid', models.SlugField(default='', max_length=25, primary_key=True, serialize=False, unique=True)),
                ('follower', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=5000000, size=10000)),
                ('following', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=5000000, size=10000)),
                ('DOB', models.DateField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Rather not ask', 'rather not ask')], max_length=25)),
                ('tags', multiselectfield.db.fields.MultiSelectField(default='', editable=False, max_length=200)),
                ('country', django_countries.fields.CountryField(default='', max_length=2)),
                ('emailId', models.EmailField(max_length=64, unique=True)),
                ('profile_pic', models.ImageField(upload_to='proupload/%Y/%m/%d/')),
            ],
        ),
    ]
