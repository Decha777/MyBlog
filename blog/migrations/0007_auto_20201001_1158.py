# Generated by Django 3.1.1 on 2020-10-01 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Programming', max_length=256),
        ),
    ]
