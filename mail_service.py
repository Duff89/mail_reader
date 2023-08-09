import imaplib
import email
import re


class MailRead:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password
        self.imap = 'imap.rambler.ru'

    def get_last_mail(self):
        """Получает последнее письмо из Входящих"""
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')

        email_message = email.message_from_string(raw_email_string)

        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')
                return body
        else:
            return email_message.get_payload()
            # return email_message.get_payload(decode=True).decode('utf-8')

    def get_password(self) -> str:
        """Достает пароль из тела письма"""
        body_mail = self.get_last_mail()
        regex = '(?<=Пароль: ).+'
        password = re.search(regex, body_mail)[0]
        return password


if __name__ == '__main__':
    last_mail = MailRead("testmail123_23@rambler.ru", 'Test12345').get_password()
