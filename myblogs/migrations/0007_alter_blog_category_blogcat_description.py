# Generated by Django 5.0.1 on 2024-01-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0006_rename_email_subscription_u_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_category',
            name='blogcat_description',
            field=models.CharField(max_length=300),
        ),
    ]