from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from celery import shared_task
from celery.schedules import crontab


@shared_task
def notify_subscribers(instance):


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


