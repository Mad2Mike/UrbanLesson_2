def send_email(message, recipient, sender='university.help@gmail.com'):
    senders = ('university.help@gmail.com', 'another@gmail.com')
    if "@" in sender and "@" in recipient and not (sender[-4:] == ".com" or sender[-3:] == ".ru" or sender[-4:] == ".net"):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender in senders:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    pass

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')