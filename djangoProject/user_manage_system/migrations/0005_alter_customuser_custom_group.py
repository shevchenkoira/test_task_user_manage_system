# Generated by Django 4.0.4 on 2022-09-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage_system', '0004_alter_customuser_custom_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='custom_group',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='user_manage_system.customgroup'),
        ),
    ]
