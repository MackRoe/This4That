# Generated by Django 2.2.6 on 2019-12-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='slug',
            field=models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=800),
        ),
    ]
