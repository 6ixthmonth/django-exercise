# Generated by Django 4.0.5 on 2022-06-30 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_rename_board_num_reply_reply_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_content',
            field=models.TextField(default='', null=True),
        ),
    ]
