Nameko-Mailgun
======================

This is a [nameko](https://nameko.readthedocs.org) service that sends an email via [Mailgun](https://mailgun.com) whenever an [event](http://nameko.readthedocs.org/en/latest/built_in_extensions.html#events-pub-sub) is received from another service.

## Table of content

- [Setup](#setup)
- [Usage](#usage)
- [Test](#test)
- [Technologies](#technologies)
- [My approach](#my-approach)
- [Improvement](#improvement)

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
(This project was initially approached with Python3.7, but there is a bug in Eventlet when used on Python 3.7.)

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

## My Approach

- As I had no experience with Python prior to this tech test, I spent a while understanding the provided code (`payments_service.py`) and the required dependencies and service (faker, nameko, mailgun, rabbitMQ).
- I started by exploring how to monitor and handle the nameko (payments) event and how to send email via mailgun.
- After completing the two tasks above, I started to write the mailing service which would handle the payments event and send the email.

## Improvement

- I found it quite difficult to write the tests for this project.
   - I only used a TDD approach when developing the email message, which is written without any dependency or service.
   - The test for sending email via mailgun is using my personal email as the recipient, which means every time running this test I would receive the email. I attempted to find a way to use a mock email but the mailgun service need the recipient to be authorised. In the future I hope to gain more knowledge on how to mock the tests in this situation.
   - It took me a while to write the nameko's integration test and but I'm still not 100% sure whether my approach was the best way to test it.
- I prefer learning by doing, so I didn't spend a lot of time on Python tutorials or reading through Python documentation before starting this project. As a result some of the syntax and structure of the code could be improved or made more 'pythonic' as I gain more experience with the language. I plan to spend more time learning Python as I found myself very interested in it after working on this test.
