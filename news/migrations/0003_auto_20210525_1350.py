# Generated by Django 2.2.2 on 2021-05-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210525_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Journalist',
        ),
    ]
