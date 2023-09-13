from django.dispatch import receiver
from django.db.models.signals import post_save

from about.models import Bill
from django.core.mail import send_mail

@receiver(post_save, sender=Bill)
def send_mails(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        email = instance.email
        comment = instance.comment
        manager_email = instance.manager_email

        email_subject = 'заявка'
        message = f'новая заявка от {name}, {email}, {comment}'
        from_email = 'xbox070@yandex.ru'
        email_manager = ['shdgit07@gmail.com', manager_email]
        send_mail(email_subject, message, from_email, email_manager)
