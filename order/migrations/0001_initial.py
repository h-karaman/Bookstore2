# Generated by Django 4.1.7 on 2023-05-20 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0003_alter_yorumlar_durum'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Siparis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=5)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('telefon', models.CharField(blank=True, max_length=20)),
                ('adres', models.CharField(blank=True, max_length=150)),
                ('sehir', models.CharField(blank=True, max_length=20)),
                ('ulke', models.CharField(blank=True, max_length=20)),
                ('alisveris_tutari', models.FloatField()),
                ('durum', models.CharField(choices=[('New', 'Yeni'), ('Accepted', 'Onaylandı'), ('Preparing', 'Hazırlanıyor'), ('OnShipping', 'Kargoya Verildi'), ('Completed', 'Tamamlandı'), ('Cancelled', 'İptal edildi')], default='Yeni', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('bilginotu', models.CharField(blank=True, max_length=100)),
                ('olusturulma_zamani', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_zamani', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiparisUrunu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urun_adedi', models.IntegerField()),
                ('price', models.FloatField()),
                ('urun_tutari', models.FloatField()),
                ('durum', models.CharField(choices=[('New', 'Yeni'), ('Accepted', 'Onayla'), ('Cancelled', 'İptal Et')], default='Yeni', max_length=10)),
                ('olusturulma_zamani', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_zamani', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.books')),
                ('siparis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.siparis')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlisverisSepeti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urun_adedi', models.IntegerField()),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.books')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
