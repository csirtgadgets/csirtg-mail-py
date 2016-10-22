import csirtg_mail

TEST_FILE = 'samples/email/multi_mixed_html_application_octet-stream_01.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == 'Noreply941@pcgamesupply.com'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith('<html><head>')
    assert results[0]['mail_parts'][1]['filename'].startswith('PP-015-725-201-298.html')

