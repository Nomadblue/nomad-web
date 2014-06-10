from django.db import models
from django.core.urlresolvers import reverse

from nomadblog.models import Post


class NomadPost(Post):
    summary = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        # URLconf for non-country blog configurations
        category = self.categories.latest('id')
        return reverse('post_detail', kwargs={'category_slug': category.slug, 'slug': self.slug})


# This code here to be used alogn with the {% generateimage %} imagekit template tag
# http://django-imagekit.readthedocs.org/en/latest/#generateimage
# https://github.com/matthewwithanm/django-imagekit/issues/202
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill


class BlogUserAvatarThumbnail(ImageSpec):
    processors = [ResizeToFill(80, 80)]
    format = 'PNG'
    options = {'quality': 90}

register.generator('nomadblog:bloguser', BlogUserAvatarThumbnail)
