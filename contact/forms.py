from django.forms import ModelForm
from contact.models import Contact
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
