# django imports
from django.template import Library
from django.utils.safestring import mark_safe

from lfs_downloadable_products import views
register = Library()


@register.simple_tag(takes_context=True)
def manage_attachments(context, product):
    request = context.get('request', None)
    result = views.manage_attachments(request, product, True)
    return mark_safe(result)


@register.inclusion_tag('lfs_downloadable_products/display_attachments.html', takes_context=True)
def downloadable_attachments(context, order):
    from lfs_downloadable_products.models import ProductUrl

    urls = []
    exists = {}
    for url in ProductUrl.objects.filter(order=order).order_by("-creation_date"):
        if url.attachment.id not in exists:
            urls.append(url)
        exists[url.attachment.id] = 1
    return {"urls" : urls}
