# Generated by Django 4.1.7 on 2023-05-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alisverissepeti',
            name='bookname',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
