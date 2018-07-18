import requests
import config

from mail_message import message

def send_email(payload):

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(config.sandbox)
    sender = 'student.com <postmaster@{0}>'.format(config.sandbox)
    recipient = '{0} <{1}>'.format(payload['payee']['name'], payload['payee']['email'])

    request = requests.post(
        request_url,
        auth=('api', config.key),
        data={
        'from': sender,
        'to': recipient,
        'subject': 'Payment Received',
        'text': message(payload)
    })

    return request
