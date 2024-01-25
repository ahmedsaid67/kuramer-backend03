from celery import shared_task
from django.core.mail import send_mail
from .models import Abone
from django.template.loader import render_to_string

from django.conf import settings



@shared_task
def send_bulk_email(bulten_basligi, pdf_url):
    subscribers = Abone.objects.filter(durum=True, is_removed=False)
    for subscriber in subscribers:
        html_content = render_to_string('email/email_template.html', {
            'bulten_basligi': bulten_basligi,
            'pdf_url': pdf_url
        })

        send_mail(
            subject="Kuramer Bülten",  # E-posta konu başlığı
            message='',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscriber.email],
            html_message=html_content,
            fail_silently=False,
        )



import time
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import get_connection
from .models import Abone


@shared_task
def send_newsletter(bulten_basligi, pdf_url,bulten_icerik):
    # Aboneleri filtreleyin
    subscribers = Abone.objects.filter(durum=True, is_removed=False)

    # SMTP Bağlantısını oluştur
    connection = get_connection()

    # E-posta gönderimi için bekleme süresi (saniye cinsinden)
    wait_time = 5  # Örneğin, her e-posta arasında 5 saniye bekleyin

    # Her aboneye e-posta gönder
    for subscriber in subscribers:
        html_content = render_to_string('email/email_template.html', {
            'bulten_basligi': bulten_basligi,
            'pdf_url': pdf_url,
            'bulten_icerik': bulten_icerik,

        })

        email = EmailMessage(
            subject=bulten_basligi,
            body=html_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[subscriber.email],
            connection=connection,
        )

        email.content_subtype = 'html'  # E-postanın HTML formatında olduğunu belirt
        email.send()

        # Her gönderim arasında belirli bir süre bekle
        time.sleep(wait_time)

    # Bağlantıyı kapat
    connection.close()



def send_newsletter01(bulten_basligi, pdf_url,bulten_icerik):
    # Aboneleri filtreleyin
    subscribers = Abone.objects.filter(durum=True, is_removed=False)

    # SMTP Bağlantısını oluştur
    connection = get_connection()

    # E-posta gönderimi için bekleme süresi (saniye cinsinden)
    wait_time = 5  # Örneğin, her e-posta arasında 5 saniye bekleyin

    # Her aboneye e-posta gönder
    for subscriber in subscribers:
        html_content = render_to_string('email/email_template.html', {
            'bulten_basligi': bulten_basligi,
            'pdf_url': pdf_url,
            'bulten_icerik': bulten_icerik,

        })

        email = EmailMessage(
            subject=bulten_basligi,
            body=html_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[subscriber.email],
            connection=connection,
        )

        email.content_subtype = 'html'  # E-postanın HTML formatında olduğunu belirt
        email.send()

        # Her gönderim arasında belirli bir süre bekle
        time.sleep(wait_time)

    # Bağlantıyı kapat
    connection.close()
