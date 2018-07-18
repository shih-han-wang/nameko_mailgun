from nameko.events import event_handler

from payments_service import PaymentService
from mail_sending import send_email

class MailingService:
    name = "mailing"

    @event_handler("payments", "payment_received")
    def handle_event(self, payload):
        print("payment received:", payload)
        send_email(payload)
