# Generated by Django 2.2.5 on 2019-09-15 22:34

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_used_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_proposal',
            field=models.FileField(default='dumy', upload_to=project.models.project_proposal_upload_path),
            preserve_default=False,
        ),
    ]
