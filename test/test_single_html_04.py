import csirtg_mail
from csirtg_mail.constants import PYVERSION

TEST_FILE = 'samples/email/single_html_04.eml'

if PYVERSION > 2:
    with open(TEST_FILE, encoding='latin-1') as f:
        email = f.read()
        email = str(email)
else:
    with open(TEST_FILE, encoding='utf8') as f:
        email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<Pineda_Tammie@exasex.com>'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith(
        '\n<!doctype html>\n<html')


def test_extract_urls():
    assert "http://a1.to/JiyPY1" in results[0]['urls']
