# Generated by Django 4.1.5 on 2023-01-13 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_comment_blog_commen_created_0e6ed4_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created'], 'verbose_name': 'Коментарий'},
        ),
    ]
