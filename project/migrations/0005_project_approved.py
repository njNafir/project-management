# Generated by Django 2.2.5 on 2019-09-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_project_proposal'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
