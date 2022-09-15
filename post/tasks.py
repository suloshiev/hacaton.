from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Contact
from social_app.celery import app




@app.task
def send_post_info(name):
    html_message2 = render_to_string('send_mail.html', {'name': name})
    for user in Contact.objects.all():
        print(user)
        send_mail(
            'Социяальная сеть студента Makers',
            '', # текст сообщения
            'suloshiev0@gmail.com', # от кого
            [user.email],
            html_message=html_message2
            
        )
