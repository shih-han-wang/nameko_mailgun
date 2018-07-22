from mailgun_api import MailgunApi
import requests

def test_send_email():

    session = requests.Session()
    mailgun = MailgunApi(session)

    authorized_recipient_email = {
    'client': {'name': 'Isaac Hughes', 'email': 'burnschristy@example.org'},
    'payee': {'name': 'Nico', 'email': 'shihhanwang930@gmail.com'},
    'payment': {'amount': 9984, 'currency': 'EUR'}}

    assert mailgun.send_email(authorized_recipient_email).status_code == 200
