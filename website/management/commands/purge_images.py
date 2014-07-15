from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import get_model
from django.core.exceptions import ImproperlyConfigured


class Command(BaseCommand):
    """
    While using databases restored from other environments (e.g. staging
    or prod) image objects will exist but, as they reference file paths non
    existing in our local machine, we will get an exception. Removing
    image objects will fix this and, if you have it configured in
    your project properly, show default images.

    Usage: add all models in your application storing images with this
    setting containing a list or tuple of two-value tuples:

        PURGE_IMAGES_FROM_MODELS = (
            ('app.FirstModel', 'image_field_name'),
            ('app.SecondModel', 'image_field_name'),
            ...
        )
    """
    help = 'Set all model image fields to None'

    def handle(self, *args, **options):

        for model_setting in getattr(settings, 'PURGE_IMAGES_FROM_MODELS', []):
            try:
                app_label, model_name = model_setting[0].split('.')
            except ValueError:
                raise ImproperlyConfigured("PURGE_IMAGES_FROM_MODELS must be a list of 2-item tuples containing ('app_label.model_name', 'image_field')")
            model = get_model(app_label, model_name)
            if model is None:
                raise ImproperlyConfigured("'%s' refers to model '%s' that has not been installed" % (model_setting, model))

            image_field = model_setting[1]
            params = {image_field: ''}
            model.objects.all().update(**params)

        self.stdout.write("Successfully set all image fields to ''")
