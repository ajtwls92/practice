# Generated by Django 4.1.1 on 2022-09-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_alter_question_question_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=200),
        ),
    ]
