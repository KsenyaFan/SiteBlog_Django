import smtplib, ssl

from_addr = "kravchenkoksuha@yandex.ru"
to_addr = "recipient@example.com"
password = "bapjbehgjsvcitjw"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.yandex.com", 465, context=context) as server:
    server.login(from_addr, password)   # здесь произойдёт проверка
    server.sendmail(from_addr, to_addr, "Subject: Test\n\nTest message")

print("Письмо отправлено!")

