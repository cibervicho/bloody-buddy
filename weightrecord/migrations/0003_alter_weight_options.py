# Generated by Django 4.2.5 on 2023-11-05 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weightrecord', '0002_alter_weight_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['id'], 'verbose_name': 'Weight Record', 'verbose_name_plural': 'Weight Records'},
        ),
    ]
