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

## My Approach

- As I have no experience with Python before this tech test, I spent a while understanding the provided code (`payments_service.py`) and the required dependencies and service (faker, nameko, mailgun, rabbitMQ).
- I started with exploring how to monitor and handle the nameko (payments) event, and then exploring how to send email via mailgun.
- After making the above two tasks work, I started to write the mailing service which would handle the payments event and send the email.

## Improvement

- I found it quite difficult to write the tests for this project.
   - The only part I used TDD approach is the email message, which is written without any dependency or service.
   - The test for sending email via mailgun is using my personal email to be recipient, which means every time running this test, I would receive the email. I was trying to find a way to mock it, but the mailgun service need the recipient to be authorised. Therefore I'd left it like this for now and will gain more knowledge about mocking the tests in this situation in the future.
   - It took me a while to write the nameko's integration test, but I'm still not 100% sure if this is the best way to test it.
- I prefer learning by doing, thus I didn't follow any Python tutorial or read through Python documentation before starting this project. Therefore I guess some code's syntax and structure might not be written precisely. I would like to spend some time in the future truly picking up Python as I found myself very interested in it after working on this test.
