from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __unicode__(self):
        return self.name


# ######### SIGNALS ##########


def send_contact_notification(sender, instance, created, **kwargs):
    if created:
        if getattr(settings, 'SEND_EMAIL_NOTIFICATIONS', False):
            from_email = settings.DEFAULT_FROM_EMAIL
            headers = {
                'From': 'Nomad-web <%s>' % from_email,
            }
            recipients = ['hector@nomadblue.com']
            subject = 'New contact form'
            plaintext_body = 'New contact from %s (%s): %s' % (instance.name, instance.email, instance.message)
            html_body = '<p>New contact from %s (%s):</p><p>%s</p>' % (instance.name, instance.email, instance.message)
            msg = EmailMultiAlternatives(subject, plaintext_body, from_email, recipients, headers=headers)
            if html_body:
                msg.attach_alternative(html_body, 'text/html')
            msg.send()

post_save.connect(send_contact_notification, sender=Contact)
