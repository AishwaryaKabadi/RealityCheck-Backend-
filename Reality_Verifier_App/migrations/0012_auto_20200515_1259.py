# Generated by Django 2.2.11 on 2020-05-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reality_Verifier_App', '0011_auto_20200515_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='images',
            field=models.ImageField(default='', upload_to='', verbose_name='images'),
            preserve_default=False,
        ),
    ]