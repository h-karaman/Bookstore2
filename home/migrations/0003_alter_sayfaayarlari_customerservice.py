# Generated by Django 4.1.7 on 2023-05-12 11:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sayfaayarlari_customerservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sayfaayarlari',
            name='customerservice',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]