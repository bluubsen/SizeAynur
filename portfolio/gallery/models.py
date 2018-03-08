from django.utils.translation import ugettext_lazy as _
from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey


class GalleryPage(Page):
    """ Displays a featured image to represent a set of gallery images. """

    featured_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        verbose_name=_("featured image"), null=True,
    )
    client_name = models.CharField(
        verbose_name=_("client name"),
        max_length=100,
        blank=True, null=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('client_name'),
        InlinePanel('gallery_images', label=_("gallery images")),
    ]


class GalleryImage(Orderable):
    """ Individual image that can be sorted into a GalleryPage."""

    page = ParentalKey(
        GalleryPage,
        on_delete=models.PROTECT,
        related_name='gallery_images',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name=_("image"),
    )

    panels = [
        ImageChooserPanel('image'),
    ]


class VideoPage(Page):
    """ Creates page for list in main menu that displays all videos."""

    content_panels = Page.content_panels + [
        InlinePanel('videos', label=_("videos")),
    ]


class Video(Orderable):
    page = ParentalKey(
        VideoPage,
        on_delete=models.PROTECT,
        related_name='videos',
    )
    client_name = models.CharField(
        verbose_name=_("client name"),
        max_length=100,
        blank=True, null=True,
    )
    video_url = models.URLField(
        verbose_name=_('video URL')
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name=_("image"),
        null=True,
    )

    panels = [
        FieldPanel('client_name'),
        FieldPanel('video_url'),
        ImageChooserPanel('image'),
    ]
