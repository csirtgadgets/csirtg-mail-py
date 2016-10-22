import csirtg_mail

TEST_FILE = 'samples/email/single_html_04.eml'

with open(TEST_FILE, encoding='latin-1') as f:
    email = f.read()
    email = str(email)

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<Pineda_Tammie@exasex.com>'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith('\n<!doctype html>\n<html')


def test_extract_urls():
    assert "http://a1.to/JiyPY1" in results[0]['urls']
