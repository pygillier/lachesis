# Generated by Django 4.2.5 on 2023-09-23 20:15

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('redirections', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redirection',
            name='key',
        ),
        migrations.AddField(
            model_name='redirection',
            name='slug',
            field=models.SlugField(default='ddd', max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='redirection',
            name='redirection_code',
            field=model_utils.fields.StatusField(choices=[('301', '301'), ('302', '302')], default='301', max_length=100, no_check_for_status=True),
        ),
    ]
