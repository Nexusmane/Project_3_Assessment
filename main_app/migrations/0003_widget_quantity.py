# Generated by Django 3.2.9 on 2022-01-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_item_widget_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
