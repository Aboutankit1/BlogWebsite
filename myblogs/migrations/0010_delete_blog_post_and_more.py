# Generated by Django 5.0.1 on 2024-01-23 06:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0009_blog_post_blog_cat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blog_post',
        ),
        migrations.AlterField(
            model_name='blog_category',
            name='blogcat_description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]