# Generated by Django 3.2.4 on 2022-02-20 19:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_comment_lesson_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
