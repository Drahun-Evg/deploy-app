from django.conf import settings
from django.core.mail import send_mail


def send(owner_email, text_1, owner_n):
    send_mail(
        'Ответ службы поддержки сайта',
        f'Здравствуйте {owner_n} \n'
        f'Новое сообщение \n\n'
        f'{text_1}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[owner_email],
        fail_silently=False,
        auth_user='TeamSupport',
    )
