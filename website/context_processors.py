from django.conf import settings


def template_extra_context(request):
    return getattr(settings, 'TEMPLATE_EXTRA_CONTEXT', {})
