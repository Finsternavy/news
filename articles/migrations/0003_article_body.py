# Generated by Django 4.0.6 on 2022-07-21 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220721_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]