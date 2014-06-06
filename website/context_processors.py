from django.conf import settings


def template_devel_helpers(request):
    return getattr(settings, 'TEMPLATE_DEVEL_HELPERS', {})
