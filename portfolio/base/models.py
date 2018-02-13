from django.utils.translation import ugettext_lazy as _
from gallery.models import GalleryPage

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


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
        context = super().get_context(request)
        context['galleries'] = GalleryPage.objects.all().live()
        return context


class RichTextPage(Page):
    body = RichTextField(blank=True, verbose_name=_("content"))

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
