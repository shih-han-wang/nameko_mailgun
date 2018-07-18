from mail_message import message

def test_message():

    mock_payment = {
    'client': {'name': 'Lauren Kelly', 'email': 'nicholaschang@example.org'},
    'payee': {'name': 'Donna Simmons', 'email':'fhernandez@example.com'},
    'payment': {'amount': 6328, 'currency': 'EUR'}}

    expect_message = '''
    Dear Donna Simmons,

    You have received a payment of 6328 EUR from Lauren Kelly (nicholaschang@example.org).

    Yours,
    student.com
    '''

    assert message(mock_payment) == expect_message
