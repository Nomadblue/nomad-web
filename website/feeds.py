from django.contrib.syndication.views import Feed
from django.db.models import Q

from nomadblog import get_post_model


# Remember to put the right Site value at admin/sites/site/ (not example.com!)
# and validate the feed with the W3C tool: http://validator.w3.org/feed/


POST_MODEL = get_post_model()


class LatestEntries(Feed):
    title = "Nomadblue.com"
    link = "/"
    description = "Nomadblue.com: Latest entries"

    def items(self):
        return POST_MODEL.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


class LatestEntriesDjango(Feed):
    title = "Nomadblue.com"
    link = "/blog/django/"
    description = "Nomadblue.com: Latest entries in Django category"

    def items(self):
        return POST_MODEL.objects.filter(categories__name__iexact='django').order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


class LatestEntriesPython(Feed):
    title = "Nomadblue.com"
    link = "/blog/python/"
    description = "Nomadblue.com: Latest entries in Python category"

    def items(self):
        return POST_MODEL.objects.filter(Q(categories__name__iexact='django') | Q(categories__name__iexact='python')).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
