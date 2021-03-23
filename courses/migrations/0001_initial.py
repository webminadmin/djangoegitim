# Generated by Django 3.1.5 on 2021-02-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kurs adini giriniz', max_length=20, unique=True, verbose_name='Kurs Adı')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Kurs Açıklaması')),
                ('date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='courses/x.jpg', upload_to='courses/%y/%m/%d')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
