import csirtg_mail

TEST_FILE = 'samples/email/multi_alternative_plain_text_01.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<suppbaby@example.com>'


def test_message_parts():
    ascii_encoded_body = results[0]['mail_parts'][0]['decoded_body'].encode('ascii', 'xmlcharrefreplace')
    assert ascii_encoded_body.decode('utf-8').startswith("Dear O&#195;&#185")


def test_extract_urls():
    urls = set(results[0]['urls'])
    assert 'http://www.geldfa.de/3957/generic-ranitidine-online-pharmacy-canadian-zantac-compresse' in urls
