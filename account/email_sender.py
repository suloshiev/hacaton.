from django.core.mail import send_mail



def send_register_email(code, email):
    full_link = f'http://localhost:8000/account/active/{code}'
    send_mail(
        'From shop project',
        full_link,
        'suloshiev0@gmail.com',
        [email]
    )


def forgot_password_email(code, email):
    send_mail(
        'Восстановление пароля',
        f'Ваш код подтверждения: {code}',
        'suloshiev0@gmail.com',
        [email]
    )