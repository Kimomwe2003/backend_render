# Generated by Django 5.1.4 on 2025-01-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschoolapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(default='Johnson', max_length=20),
        ),
    ]
