# Generated by Django 3.1.1 on 2020-10-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201001_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='admin', max_length=256),
        ),
    ]