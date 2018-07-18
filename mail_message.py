def message(payload):

    payee = payload['payee']['name']
    amount = payload['payment']['amount']
    currency = payload['payment']['currency']
    client = payload['client']['name']
    email = payload['client']['email']

    message = '''
    Dear {},

    You have received a payment of {} {} from {} ({}).

    Yours,
    student.com
    '''.format(payee, amount, currency, client, email)

    return message
