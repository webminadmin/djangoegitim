# Generated by Django 3.1.5 on 2021-03-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('soyad', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=11)),
                ('mesaj', models.TextField(blank=True)),
            ],
        ),
    ]
