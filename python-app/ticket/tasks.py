from support.celery import app

from .service import send


@app.task
def send_answer_email(owner_email, text_1, owner_n):
    send(owner_email, text_1, owner_n)
