from nameko.events import event_handler
from payments import PaymentService

class MailingService:
    name = "mailing"

    @event_handler("payments", "payment_received")
    def handle_event(self, payload):
        print("payment received:", payload)
