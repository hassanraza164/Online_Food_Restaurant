# Generated by Django 2.2.7 on 2019-11-26 14:23

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_remove_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='created'),
        ),
    ]
