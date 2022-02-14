# Generated by Django 4.0.2 on 2022-02-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_book_register_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_register',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_register',
            name='review',
            field=models.CharField(default=0, max_length=120),
        ),
    ]