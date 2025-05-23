# Generated by Django 5.1.7 on 2025-04-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0007_alter_bookimage_image"),
        ("wishlist", "0003_alter_wishlist_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="wishlist",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="wishlist",
            name="book",
        ),
        migrations.AddField(
            model_name="wishlist",
            name="book",
            field=models.ManyToManyField(related_name="wishlists", to="book.book"),
        ),
    ]
