# Generated by Django 5.1.4 on 2025-01-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_translations'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytranslation',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories'),
        ),
    ]