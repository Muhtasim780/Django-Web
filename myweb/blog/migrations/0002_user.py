# Generated by Django 2.2.7 on 2019-12-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_ID', models.CharField(max_length=100)),
                ('contact', models.ImageField(max_length=15, upload_to='')),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
