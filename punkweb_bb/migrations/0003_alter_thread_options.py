# Generated by Django 4.2.11 on 2024-05-29 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("punkweb_bb", "0002_thread_view_count"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="thread",
            options={
                "ordering": ("subcategory", "-is_pinned", "-last_post_created_at"),
                "permissions": (
                    ("pin_thread", "Can pin thread"),
                    ("close_thread", "Can close thread"),
                ),
            },
        ),
    ]
