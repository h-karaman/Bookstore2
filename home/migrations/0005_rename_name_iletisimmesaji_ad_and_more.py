# Generated by Django 4.1.7 on 2023-04-20 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_mesaj_iletisimmesaji_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iletisimmesaji',
            old_name='name',
            new_name='ad',
        ),
        migrations.RenameField(
            model_name='iletisimmesaji',
            old_name='subject',
            new_name='konu',
        ),
        migrations.RenameField(
            model_name='iletisimmesaji',
            old_name='message',
            new_name='mesaj',
        ),
    ]