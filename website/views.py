from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from propaganda.models import Subscriber
from contact.models import Contact, PitchContact


class NomadPageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(NomadPageView, self).get_context_data(**kwargs)
        from blog.models import NomadPost
        context['posts'] = NomadPost.objects.order_by('-pub_date')[:3]
        return context


class ContactCreateView(CreateView):
    model = Contact
    success_url = reverse_lazy('contact_success')


class PitchContactCreateView(CreateView):
    model = PitchContact
    success_url = reverse_lazy('pitchcontact_success')


class SubscriberCreateView(CreateView):
    model = Subscriber
    template_name = 'subscriber_form.html'
    success_url = reverse_lazy('home')
