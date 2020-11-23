import csirtg_mail

TEST_FILE = 'samples/email/multi_mixed_alternative_plain_html_01.eml'

with open(TEST_FILE, encoding='utf8') as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers_from():
    assert results[0]['headers']['from'][0].startswith('Bobbi Summerfield')


def test_message_headers_reply_to():
    assert results[0]['headers']['reply-to'][0].startswith('king')


def test_message_headers_to():
    assert results[0]['headers']['to'][0].startswith('king')


def test_message_headers_subject():
    assert results[0]['headers']['subject'][0].startswith(
        'Changes in Your Booking Nr:48322')
