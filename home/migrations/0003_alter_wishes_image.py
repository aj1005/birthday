# Generated by Django 4.1.3 on 2022-11-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_wishes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='image',
            field=models.ImageField(default='default/default.png', upload_to=''),
        ),
    ]
