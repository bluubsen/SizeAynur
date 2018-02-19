from django.utils.translation import ugettext_lazy as _
from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image, AbstractImage, AbstractRendition

from modelcluster.fields import ParentalKey


class GalleryPage(Page):
    """ Displays a featured image to represent a set of gallery images. """
    featured_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        verbose_name=_("featured image"), null=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        InlinePanel('gallery_images', label=_("gallery images")),
    ]


class Img(AbstractImage):
    client_name = models.CharField(
        verbose_name=_("client name"),
        max_length=100,
        blank=True, null=True,
    )
    client_url = models.URLField(
        verbose_name=_("client url"),
        blank=True, null=True,
    )

    admin_form_fields = (
        'title',
        'file',
        'client_name',
        'client_url',
        'focal_point_x',
        'focal_point_y',
        'focal_point_width',
        'focal_point_height',
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(Img, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )


class GalleryImage(Orderable):
    """ Individual image that can be sorted into a GalleryPage."""
    page = ParentalKey(
        GalleryPage,
        on_delete=models.PROTECT,
        related_name='gallery_images',
    )
    image = models.ForeignKey(
        'gallery.Img',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name=_("image"),
    )

    panels = [
        ImageChooserPanel('image'),
    ]
