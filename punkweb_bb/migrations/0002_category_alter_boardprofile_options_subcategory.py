# Generated by Django 4.2.4 on 2023-08-20 17:04

from django.db import migrations, models
import django.db.models.deletion
import precise_bbcode.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('punkweb_bb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('_description_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('description', precise_bbcode.fields.BBCodeTextField(blank=True, no_rendered_field=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['order'],
            },
        ),
        migrations.AlterModelOptions(
            name='boardprofile',
            options={'ordering': ['user__username']},
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('_description_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('description', precise_bbcode.fields.BBCodeTextField(blank=True, no_rendered_field=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='punkweb_bb.category')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
                'ordering': ['category__order', 'order'],
            },
        ),
    ]
