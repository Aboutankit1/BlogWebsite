# Generated by Django 5.0.1 on 2024-01-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_cat', models.CharField(max_length=60, unique=True)),
                ('blogcat_img', models.ImageField(upload_to='images/')),
                ('blogcat_description', models.CharField(max_length=200)),
            ],
        ),
    ]