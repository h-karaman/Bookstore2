# Generated by Django 4.1.7 on 2023-05-12 14:10

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_sayfaayarlari_customerservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='sayfaayarlari',
            name='freeshipping',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sayfaayarlari',
            name='qualityproduct',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sayfaayarlari',
            name='returniade',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sayfaayarlari',
            name='support724',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
