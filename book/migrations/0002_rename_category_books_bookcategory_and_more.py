# Generated by Django 4.1.7 on 2023-04-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='category',
            new_name='bookcategory',
        ),
        migrations.AddField(
            model_name='books',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='books',
            name='translated_by',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='detail',
            field=models.TextField(max_length=255),
        ),
    ]
