from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic import TemplateView

from website.views import ContactCreateView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', ContactCreateView.as_view(), name='contact_form'),
    url(r'^success/$', TemplateView.as_view(template_name='contact/contact_success.html'), name='contact_success'),
)
