# Generated by Django 4.1.7 on 2023-04-21 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_ad_iletisimmesaji_adsoyad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iletisimmesaji',
            old_name='adsoyad',
            new_name='ad_soyad',
        ),
    ]