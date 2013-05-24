# django imports
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# lfs imports
from lfs.catalog.models import Product
from lfs.order.models import Order


class ProductAttachment(models.Model):
    """
    Represents a downloadable attachment of a product.

    **Attributes:**

    title
        The title of the attachment

    description
        The description of the attachment

    file
        The downloadable file of the attachment

    product
        The product the attachment belongs to

    position
        The position of the attachment within a product.
    """
    title = models.CharField(_(u"Title"), max_length=50)
    description = models.TextField(_(u"Description"), blank=True)
    file = models.FileField(upload_to="downloadable_products")
    image = models.FileField(upload_to="downloadable_products/previews")
    product = models.ForeignKey(Product, verbose_name=_(u"Product"), related_name="downloadable_attachments")
    position = models.IntegerField(_(u"Position"), default=1)

    class Meta:
        ordering = ("position", )

    def get_filename(self):
        """
        Returns the plain filename (without any path information)
        """
        try:
            name = self.file.name.split("/")[-1]
        except (IndexError, AttributeError):
            name = self.file.name

        # "HTTP response headers must be in US-ASCII format"
        try:
            return name.encode("utf-8")
        except:
            return name

    def get_url(self):
        if self.file.url:
            return self.file.url
        return None


class ProductUrl(models.Model):
    """
    """
    attachment = models.ForeignKey(ProductAttachment, verbose_name=_(u"Attachment"))
    order = models.ForeignKey(Order, verbose_name=_(u"Order"))
    url = models.CharField(_(u"URL"), max_length=50)
    creation_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
