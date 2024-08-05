from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post

@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):

    subscribers_list = instance.categories.subscribers.all()
    for subscriber in subscribers_list:
        html_content = render_to_string(
            'news_cat.html',
            {
                'post': instance,
                'post_author': subscriber.username
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'{instance.article}',
            body=f'Здравствуй, {instance.categories}. Новая статья в твоём любимом разделе!',
            from_email='awercool@yandex.by',
            to=[subscriber.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()