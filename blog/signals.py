from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from .models import Contact

@receiver(post_save, sender=Contact)
def send_new_notification_email(sender, instance, created, **kwargs):
    if created:
        subject = "New Entry in contact Form"
        emailid = instance.Email
        msg = instance.Message

        message = f'Email Id: {emailid} \n Message: {msg}'

        send_mail(
            subject,
            message,
            'vikaspadhi5@gmail.com',['v.padhi@somaiya.edu' , 'mohit.joshi@kudosware.com'],
            fail_silently=False,
        )
