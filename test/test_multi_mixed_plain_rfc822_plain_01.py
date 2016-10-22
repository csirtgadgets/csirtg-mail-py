import csirtg_mail

TEST_FILE = 'samples/email/multi_mixed_plain_rfc822_plain_01.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<john@csirtgadgets.org>'
    assert results[1]['headers']['to'][0] == 'John <john@csirtgadgets.org>'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith('give me your credentials')
    assert results[1]['mail_parts'][0]['decoded_body'].startswith('phishing message attached')


def test_extract_urls():
    assert "http://www.example.com" in results[0]['urls']

