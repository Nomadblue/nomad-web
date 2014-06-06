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
