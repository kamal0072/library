# Generated by Django 5.0.4 on 2024-05-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='bookImages')),
                ('author', models.CharField(default='Chetan Bhagat..', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField(default='Library for various books')),
                ('book_soft_copy', models.FileField(upload_to='bookSoftcopy')),
            ],
        ),
    ]
