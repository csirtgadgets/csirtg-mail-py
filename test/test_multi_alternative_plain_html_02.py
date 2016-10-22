import csirtg_mail

TEST_FILE = 'samples/email/multi_alternative_plain_html_02.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['delivered-to'][0] == 'john@csirtgadgets.org'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith('http://www.indiana.edu')
    assert results[0]['mail_parts'][1]['decoded_body'].startswith('<div dir="ltr"')


def test_extract_urls():
    assert "http://www.indiana.edu" in results[0]['urls']

