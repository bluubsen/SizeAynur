from django.utils.translation import ugettext_lazy as _
from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from gallery.models import GalleryPage, GalleryImage
from modelcluster.fields import ParentalKey


class LandingPage(Page):
    """ The first page that greets the visitor. """

    text = RichTextField(blank=True, verbose_name=_("content"))

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        InlinePanel('landing_images', label=_("gallery images")),
    ]


class LandingImage(Orderable):
    """ Individual image that can be added into LandingPage."""

    page = ParentalKey(
        LandingPage,
        on_delete=models.PROTECT,
        related_name='landing_images',
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


class PortfolioPage(Page):
    """ Creates page with optional richtext that displays all galleries.
    Redirects with 200 to another model and template. It's good for a root
    '/' if you want that URL to display a child element. For the sake of
    simplicity, this has to be hard-coded."""

    body = RichTextField(blank=True, verbose_name=_("content"))

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        context = super(PortfolioPage, self).get_context(request)
        context['galleries'] = GalleryPage.objects.all().live()
        return context


class RichTextPage(Page):
    body = RichTextField(blank=True, verbose_name=_("content"))
    profile = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name=_("optional profile image"),
        null=True, blank=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('profile'),
        FieldPanel('body', classname="full"),
    ]
