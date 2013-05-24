# python imports
import random
import string


def create_url():
    """
    Creates a unique 50 figure string.
    """
    from lfs_downloadable_products.models import ProductUrl
    while 1:
        url =  "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(50)])
        try:
            ProductUrl.objects.get(url=url)
        except ProductUrl.DoesNotExist:
            return url
