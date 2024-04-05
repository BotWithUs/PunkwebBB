# Generated by Django 4.2.11 on 2024-04-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("punkweb_bb", "0009_remove_category__description_rendered_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="boardprofile",
            options={"ordering": ("user__username",)},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("order",),
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("created_at",)},
        ),
        migrations.AlterModelOptions(
            name="shout",
            options={"ordering": ("-created_at",)},
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={
                "ordering": ("category__order", "order"),
                "verbose_name": "subcategory",
                "verbose_name_plural": "subcategories",
            },
        ),
        migrations.AlterModelOptions(
            name="thread",
            options={"ordering": ("subcategory", "-is_pinned", "-created_at")},
        ),
        migrations.AddField(
            model_name="thread",
            name="is_closed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="thread",
            name="is_pinned",
            field=models.BooleanField(default=False),
        ),
    ]
