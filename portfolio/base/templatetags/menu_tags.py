from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


@register.assignment_tag(takes_context=True)
def top_menu(context, parent, calling_page=None):
    return parent.get_children().live().in_menu()
