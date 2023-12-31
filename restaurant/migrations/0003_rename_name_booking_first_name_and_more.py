# Generated by Django 5.0 on 2023-12-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_menuitem_rename_bookingdate_booking_booking_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="name",
            new_name="first_name",
        ),
        migrations.RenameField(
            model_name="menu",
            old_name="title",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="menu",
            name="inventory",
        ),
        migrations.AddField(
            model_name="menu",
            name="menu_item_description",
            field=models.TextField(default="", max_length=1000),
        ),
    ]
