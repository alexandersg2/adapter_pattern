from abc import abstractmethod


class SMSMessage:
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_body(self, body):
        self.body = body
    
    def send(self):
        print(
            f"""
            Sending an SMS message to: {self.phone_number}
            Body: {self.body}
            """
        )
        return True


class BaseNotification:
    
    @abstractmethod
    def set_recipient(self, recipient):
        ...
    
    @abstractmethod
    def set_subject(self, subject):
        ...
    
    @abstractmethod
    def set_body(self, body):
        ...
    
    @abstractmethod
    def send(self):
        ...


class EmailNotification(BaseNotification):

    def set_recipient(self, recipient):
        self.recipient = recipient
    
    def set_subject(self, subject):
        self.subject = subject
    
    def set_body(self, body):
        self.body = body
    
    def send(self):
        print(
            f"""
            Sending an email to: {self.recipient}
            Subject: {self.subject}
            Body: {self.body}
            """
        )
        return True


class SMSMessageAdapter(BaseNotification):

    def __init__(self, sms_message: SMSMessage):
        self.sms_message = sms_message

    def set_recipient(self, recipient):
        self.sms_message.set_phone_number(recipient)
    
    def set_subject(self, subject):
        self._subject = subject
    
    def set_body(self, body):
        self.sms_message.set_body("")
        self.sms_message.set_body(self._subject + " " + body)
    
    def send(self):
        self.sms_message.send()


class NotificationClient:

    def build_notification(notification: BaseNotification, recipient, subject, body) -> BaseNotification:
        notification.set_recipient(recipient)
        notification.set_subject(subject)
        notification.set_body(body)

        return notification

    
    def send_notification(notification: BaseNotification):
        return notification.send()


def main():
    print("Something has happened, notifying the user!")

    print("\nSending an email")
    email = NotificationClient.build_notification(
        notification=EmailNotification(),
        recipient="Alex@gmail.com",
        subject="Hello!",
        body="Hi, I'm a prince from Kenya and I'd like you to help me move $74,000,000 to your country.",
    )
    NotificationClient.send_notification(email)

    print("\nSending an SMS message")
    sms_message = NotificationClient.build_notification(
        notification=SMSMessageAdapter(SMSMessage()),
        recipient="1234567890",
        subject="Hello!",
        body="Hi, I'm a lawyer representing your late great grandfather. You're rich.",
    )
    NotificationClient.send_notification(sms_message)


if __name__ == "__main__":
    main()
