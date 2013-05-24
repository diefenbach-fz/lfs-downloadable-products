# General imports
from django.conf.urls.defaults import *

urlpatterns = patterns('lfs_downloadable_products.views',
    url(r'^product-attachments/(?P<product_id>\d*)$', "manage_attachments", name="dp_manage_attachments"),
    url(r'^add-attachment/(?P<product_id>\d*)$', "add_attachment", name="dp_add_attachment"),
    url(r'^update-attachments/(?P<product_id>\d*)$', "update_attachments", name="dp_update_attachments"),
    url(r'^move-product-attachments/(?P<id>\d+)$', "move_attachment", name="dp_move_product_attachment"),
    url(r'^download-product-attachments/(?P<url>\w+)$', "download_attachment", name="dp_download_product_attachment"),
)
