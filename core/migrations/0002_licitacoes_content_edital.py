# Generated by Django 3.2.3 on 2021-05-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='licitacoes',
            name='content_edital',
            field=models.TextField(blank=True, null=True),
        ),
    ]
