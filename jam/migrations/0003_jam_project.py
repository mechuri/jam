# Generated by Django 2.2.7 on 2019-11-30 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0002_jam_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='jam',
            name='project',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='jam.Project'),
            preserve_default=False,
        ),
    ]
