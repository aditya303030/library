# Generated by Django 4.0.3 on 2022-03-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_book_issue_date_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_issue',
            name='name_of_person',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
