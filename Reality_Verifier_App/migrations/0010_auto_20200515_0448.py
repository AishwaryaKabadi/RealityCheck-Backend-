# Generated by Django 2.2.11 on 2020-05-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reality_Verifier_App', '0009_auto_20200414_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='Original_Image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='picture',
            name='QR_Embedded_Image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
