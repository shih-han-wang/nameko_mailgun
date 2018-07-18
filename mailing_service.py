from nameko.events import event_handler
from mail_sending import send_email

# This PaymentService will raise the error when send_email function being called
# as the fake email address is not authorized recipient by mailgun
from payments_service import PaymentService

class MailingService:
    name = "mailing"

    @event_handler("payments", "payment_received")
    def handle_event(self, payload):
        print("payment received:", payload)
        send_email(payload)
