# Generated by Django 4.2 on 2023-09-09 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brenda', '0007_alter_skills_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='percentage',
            field=models.PositiveIntegerField(blank=True, max_length=30),
        ),
    ]
