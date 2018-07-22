from mail_message import message
import requests
import yaml

with open("config.yml") as ymlfile:
    cfg = yaml.load(ymlfile)

class MailgunApi:

    def __init__(self, session):
        self.session = session

    def send_email(self, payload):
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(cfg['Mailgun']['sandbox'])
        sender = 'student.com <postmaster@{0}>'.format(cfg['Mailgun']['sandbox'])
        recipient = '{0} <{1}>'.format(payload['payee']['name'], payload['payee']['email'])

        request = self.session.post(
            request_url,
            auth=('api', cfg['Mailgun']['api_key']),
            data={
            'from': sender,
            'to': recipient,
            'subject': 'Payment Received',
            'text': message(payload)
        })

        if request.status_code == requests.codes.ok:
          return request
        else:
          print('Error: {0}'.format(request.raise_for_status()))
