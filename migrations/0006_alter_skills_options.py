# Generated by Django 4.2 on 2023-09-09 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brenda', '0005_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ['name'], 'verbose_name_plural': 'Skills'},
        ),
    ]
