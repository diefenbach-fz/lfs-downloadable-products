# django imports
from django.dispatch import receiver

# lfs imports
from lfs.core.signals import order_paid

# lfs_downloadable_products imports
from lfs_downloadable_products.utils import create_url


@receiver(order_paid)
def create_download_urls(sender, **kwargs):
    """
    Creates a download urls when an order has been paid.
    """
    from lfs_downloadable_products.models import ProductUrl
    order = sender.get("order")

    for item in order.items.all():
        for attachment in item.product.downloadable_attachments.all():
            ProductUrl.objects.create(
                attachment = attachment,
                order = order,
                url = create_url(),
            )
