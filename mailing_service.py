from nameko.events import event_handler
from mailgun_webservice import MailgunWebservice

from payments_service import PaymentService

class MailingService:
    name = "mailgun"

    webservice = MailgunWebservice()

    @event_handler("payments", "payment_received")
    def handle_event(self, payload):
        print("Payment received:", payload)
        mailing = self.webservice.send_email(payload)
        print("Mailgun status:", mailing.json()['message'])
