import smtplib
from html_draft import html_draft
from api_check import get_tasks
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail():

    # Ваши данные для подключения
    sender_email = 'vasilevas12609@gmail.com'
    receiver_email_1 = 'piff12609@gmail.com'
    receiver_email_2 = 'vasilevas@alrosa.ru'
    password = 'dzed mtpr ujut kmai'
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Test рассылка"
    msg['From'] = sender_email
    # msg['To'] = (receiver_email_1, receiver_email_2)

    # Create the body of the message (a plain-text and an HTML version).
    html = ""
    for i in get_tasks():
        html_i = html_draft(task_text=i.get('title'), step_date=i.get('date'))
        html += html_i

    part = MIMEText(html, 'html')
    msg.attach(part)

    try:
        # Отправка сообщения
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(
            sender_email,
            (receiver_email_1, receiver_email_2),
            msg.as_string()
        )
        print("Сообщение успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
    finally:
        server.quit()


if __name__ == "__main__":

    send_mail()
