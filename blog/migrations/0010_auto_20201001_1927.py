# Generated by Django 3.1.1 on 2020-10-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(default='Images/header/blog_defualt.jpg', upload_to='Images/header/'),
        ),
    ]
