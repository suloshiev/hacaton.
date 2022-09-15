import time
from django.core.mail import send_mail
from social_app.celery import app


@app.task
def celery_send_confirmation_email(code, email):
    time.sleep(1) # время для выполнния в онновом режиме
    full_link = f'http://localhost:8000/account/active/{code}'
    send_mail(
        'Социальная сеть от студента Makers', # заголовок сообщения
        full_link, # текст сообщения
        'suloshiev0@gmail.com', # от кого
        [email] # кому
    )