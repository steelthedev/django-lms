# Generated by Django 3.2.4 on 2022-02-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Student', 'Instructor'), ('Student', 'Student'), ('Student', 'Admin')], default='Student', max_length=20),
        ),
    ]
