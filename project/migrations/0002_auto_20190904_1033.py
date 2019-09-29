# Generated by Django 2.1.7 on 2019-09-04 04:33

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='thumbnail',
        ),
        migrations.AddField(
            model_name='project',
            name='project_file',
            field=models.FileField(default='dummy', upload_to=project.models.file_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='group_number',
            field=models.PositiveIntegerField(),
        ),
    ]
