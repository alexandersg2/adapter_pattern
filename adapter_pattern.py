class SMSMessage:
    def __init__(self):
        self.phone_number = None
        self.body = ""
    
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


class Email:
    def __init__(self):
        self.recipient = None
        self.subject = ""
        self.body = ""

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


class SMSMessageAdapter(Email):

    def __init__(self, sms_message: SMSMessage):
        self.sms_message = sms_message
    
    def set_recipient(self, recipient):
        self.sms_message.phone_number = recipient
    
    def set_subject(self, subject):
        self._subject = subject
    
    def set_body(self, body):
        self.sms_message.body = ""
        self.sms_message.body = self._subject + " " + body
    
    def send(self):
        self.sms_message.send()


class NotificationClient:

    def build_notification(self, notification, recipient, subject, body) -> Email:
        notification.set_recipient(recipient)
        notification.set_subject(subject)
        notification.set_body(body)

        return notification

    
    def send_notification(self, notification: Email):
        return notification.send()


def main():
    print("Something has happened, notifying the user!")

    notification_client = NotificationClient()

    print("\nSending an email")
    email = notification_client.build_notification(
        Email(),
        "Alex",
        "Hello!",
        "Hi, I'm a prince from Kenya and I'd like you to help me move $74,000,000 to your country.",
    )
    notification_client.send_notification(email)

    print("\nSending an SMS Message")
    adapted_sms_message = SMSMessageAdapter(SMSMessage())
    adapted_sms_message = notification_client.build_notification(
        adapted_sms_message,
        "1234567890",
        "Hello!",
        "Hi, I'm a lawyer representing your late great grandfather. You've been left money.",
    )
    notification_client.send_notification(adapted_sms_message)


if __name__ == "__main__":
    main()
