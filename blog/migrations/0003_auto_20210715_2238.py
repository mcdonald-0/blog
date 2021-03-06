# Generated by Django 3.2.4 on 2021-07-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210715_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='birthday',
            new_name='birthdate',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lastname',
            new_name='lastn_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='middlename',
            new_name='middle_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
