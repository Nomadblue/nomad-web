from django.contrib.syndication.views import Feed
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from nomadblog import get_post_model


# Remember to put the right Site value at admin/sites/site/ (not example.com!)
# and validate the feed with the W3C tool: http://validator.w3.org/feed/


POST_MODEL = get_post_model()


class LatestEntries(Feed):
    title = _("Nomadblue - We are your CTO on-demand")
    link = "/"
    description = _("Nomadblue: Latest entries")

    def items(self):
        return POST_MODEL.objects.filter(status=POST_MODEL.PUBLIC_STATUS).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # Django storage backend for S3 with django-storages requires defining
        # STATIC_URL with absolute url. For other backends, final img_url may
        # end up being relative and incomplete, STATIC_URL prefix need be to
        # be appended (e.g. django default storage backend in development mode)
        try:
            img_url = item.pic.url
        except:
            img_url = "%simg/nomadblue_logo_fb.png" % settings.STATIC_URL
        return "<img src='%s'>%s" % (img_url, item.content)


class LatestEntriesDjango(Feed):
    title = _("Nomadblue - We are your CTO on-demand")
    link = "/blog/django/"
    description = _("Nomadblue: Latest entries in Django category")

    def items(self):
        return POST_MODEL.objects.filter(status=POST_MODEL.PUBLIC_STATUS).filter(categories__name__iexact='django').order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


class LatestEntriesPython(Feed):
    title = _("Nomadblue - We are your CTO on-demand")
    link = "/blog/python/"
    description = _("Nomadblue: Latest entries in Python category")

    def items(self):
        return POST_MODEL.objects.filter(status=POST_MODEL.PUBLIC_STATUS).filter(Q(categories__name__iexact='django') | Q(categories__name__iexact='python')).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
