# Generated by Django 4.2.2 on 2023-11-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('book_edition', models.IntegerField()),
            ],
        ),
    ]
