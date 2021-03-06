# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 20:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.wagtailcore.models
import wagtail.wagtailimages.models
import wagtail.wagtailsearch.index


class Migration(migrations.Migration):

    replaces = [('gallery', '0002_auto_20180219_1122'), ('gallery', '0003_auto_20180219_1129'), ('gallery', '0004_auto_20180219_1849'), ('gallery', '0005_auto_20180219_1859'), ('gallery', '0006_client'), ('gallery', '0007_galleryimage_client'), ('gallery', '0008_auto_20180219_1948'), ('gallery', '0009_auto_20180219_1949'), ('gallery', '0010_auto_20180219_1958'), ('gallery', '0011_auto_20180219_2010'), ('gallery', '0012_auto_20180219_2014'), ('gallery', '0013_delete_client')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.ImageField(height_field='height', upload_to=wagtail.wagtailimages.models.get_upload_to, verbose_name='file', width_field='width')),
                ('width', models.IntegerField(editable=False, verbose_name='width')),
                ('height', models.IntegerField(editable=False, verbose_name='height')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='client name')),
                ('collection', models.ForeignKey(default=wagtail.wagtailcore.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
                ('client_url', models.URLField(blank=True, null=True, verbose_name='client url')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.wagtailsearch.index.Indexed, models.Model),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image', verbose_name='image'),
        ),
        migrations.CreateModel(
            name='CustomRendition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_spec', models.CharField(db_index=True, max_length=255)),
                ('file', models.ImageField(height_field='height', upload_to=wagtail.wagtailimages.models.get_rendition_upload_to, width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(blank=True, default='', editable=False, max_length=16)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renditions', to='wagtailimages.Image')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customrendition',
            unique_together=set([('image', 'filter_spec', 'focal_point_key')]),
        ),
    ]
