# Generated by Django 2.2.11 on 2020-05-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reality_Verifier_App', '0010_auto_20200515_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='picture',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
