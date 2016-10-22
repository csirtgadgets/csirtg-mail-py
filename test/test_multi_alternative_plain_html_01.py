import csirtg_mail
from pprint import pprint

TEST_FILE = 'samples/email/multi_alternative_plain_html_01.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == 'career@walmart.com'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith(' \n\nYou have been selected')
    assert results[0]['mail_parts'][1]['decoded_body'].startswith('<!DOCTYPE HTML PUBLIC')


def test_extract_urls():
    assert "http://jobswalmart.xyz/customer/de/proc/" in results[0]['urls']

