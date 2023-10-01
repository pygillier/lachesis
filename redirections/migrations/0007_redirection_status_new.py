# Generated by Django 4.2.5 on 2023-10-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirections', '0006_alter_redirection_redirection_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirection',
            name='status_new',
            field=models.CharField(choices=[('dr', 'Draft'), ('pu', 'Published')], default='dr', max_length=2),
        ),
    ]