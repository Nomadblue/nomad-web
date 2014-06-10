from django.db import models
from django.core.urlresolvers import reverse

from imagekit import ImageSpec, register
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust

from nomadblog.models import Post


class NomadPost(Post):
    summary = models.TextField()
    image = models.ImageField(upload_to="images/posts/%Y/%m/%d", max_length=500, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        # URLconf for non-country blog configurations
        category = self.categories.latest('id')
        return reverse('post_detail', kwargs={'category_slug': category.slug, 'slug': self.slug})

    # Imagekit specs
    pic = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(720)], source='image', format='PNG', options={'quality': 90})


# This code here to be used alogn with the {% generateimage %} imagekit template tag
# http://django-imagekit.readthedocs.org/en/latest/#generateimage
# https://github.com/matthewwithanm/django-imagekit/issues/202


class BlogUserAvatarThumbnail(ImageSpec):
    processors = [ResizeToFill(80, 80)]
    format = 'PNG'
    options = {'quality': 90}

register.generator('nomadblog:bloguser', BlogUserAvatarThumbnail)
