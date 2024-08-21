def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not sender.endswith(('.com','.ru','.net') or not recipient.endswith('.com','.ru','.net')):
        print("Невозможно отправить письмо с адреса {} на адрес {}".format(sender,recipient))
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == sender:
        print('Письмо успешно отправлено с адреса {} на адрес {}'. format(sender, recipient))
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {} на адрес {}'.format(sender,recipient))



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы лучший студент курса', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

