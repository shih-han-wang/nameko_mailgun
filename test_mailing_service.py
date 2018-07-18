from nameko.standalone.events import event_dispatcher
from nameko.testing.services import entrypoint_waiter
from mailing_service import MailingService

def test_event_interface(container_factory, rabbit_config):
    container = container_factory(MailingService, rabbit_config)
    container.start()
    dispatch = event_dispatcher(rabbit_config)

    with entrypoint_waiter(container, 'handle_event'):
        dispatch("payments", "payment_received", "payload")
