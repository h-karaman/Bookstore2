# Generated by Django 4.1.7 on 2023-04-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_books_detail_yorumlar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Karton Kapak', 'Karton Kapak'), ('Kuşe Kapak', 'Kuşe Kapak')], default='None', max_length=50),
        ),
    ]