# Generated by Django 2.0.1 on 2018-01-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("papers", "0011_auto_20180111_1631")]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="arxiv_version",
            field=models.IntegerField(default=0),
            preserve_default=False,
        )
    ]
