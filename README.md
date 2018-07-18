Nameko-Mailgun
======================

This is a [nameko](https://nameko.readthedocs.org) service that sends an email via [Mailgun](https://mailgun.com) whenever an [event](http://nameko.readthedocs.org/en/latest/built_in_extensions.html#events-pub-sub) is received from another service.

## Table of content

- [Setup](#setup)
- [Usage](#usage)
- [Test](#test)
- [Technologies](#technologies)

## Setup

- Install all the dependencies, run: `pipenv install`
    - If you haven't installed Pipenv, please check [here](https://docs.pipenv.org/)
- Start RabbitMQ Server.
    - This project's Nameko’s built-in features rely on RabbitMQ. If you haven't installed RabbitMQ, please check [here](https://www.rabbitmq.com/download.html)

## Usage

- After setting up, go to its root directory and run:

```
pipenv run nameko run mailing_service
```
- The MailingService is automatically handling the events from PaymentsService(`payments_service.py`).

- Once the payment event received, you would see the information of payment details in the terminal, the following is an example:

```
starting services: mailing, payments
Connected to amqp://guest:**@127.0.0.1:5672//
payment received: {
'client': {'name': 'Frank Castro', 'email': 'christophercooper@example.org'},
'payee': {'name': 'Deborah Yang', 'email': 'rachelfox@example.net'},
'payment': {'amount': 5879, 'currency': 'GBP'}}
```
- The MailingService will then send an email via [Mailgun](https://mailgun.com) to the payee. The email example:

![email_sample](/screenshot/email_sample.png)

- Due to the reason that this PaymentsService(`payments_service.py`) contains the fake payments data created by [Faker](https://faker.readthedocs.io) and the fake email address is not the authorised-recipient from [Mailgun](https://mailgun.com), you will see the error message following the payments information. (The service has been tested by authorised recipient).

## Test

- Go to its root directory and run: `pipenv run pytest`

![pytest](/screenshot/pytest.png)

## Technologies

- Language: Python3.6
(This project was initially approached with Python3.7, but had been found out that there is a bug in Eventlet when used on Python 3.7.)

![py3.7_eventlet_bug](/screenshot/py3.7_eventlet_bug.png)

- Testing tool:
   - [pytest](https://docs.pytest.org/en/latest/)
- Virtualenv & Dependency management:
   - [pipenv]((https://docs.pipenv.org/))
- Dependencies:
   - [faker](https://faker.readthedocs.io)
   - [nameko](https://nameko.readthedocs.org)
   - [requests](http://docs.python-requests.org/en/master/)
- Email API Service:
   - [Mailgun](https://mailgun.com)
