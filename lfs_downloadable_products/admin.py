# django imports
from django.contrib import admin

# lfs imports
from lfs_downloadable_products.models import ProductAttachment
from lfs_downloadable_products.models import ProductUrl

admin.site.register(ProductAttachment)
admin.site.register(ProductUrl)
