# Generated by Django 5.0.2 on 2024-03-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='NW', max_length=20),
        ),
    ]
