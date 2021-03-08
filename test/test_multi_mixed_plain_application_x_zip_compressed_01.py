import csirtg_mail
from csirtg_mail.constants import PYVERSION

TEST_FILE = 'samples/email/multi_mixed_plain_application_x_zip_compressed_01.eml'

if PYVERSION > 2:
    with open(TEST_FILE, encoding='utf-8') as f:
        email = f.read()
else:
    with open(TEST_FILE, encoding='utf8') as f:
        email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['to'][0] == 'Larry <larry@example.com>'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith(
        'See the attached zip file')
    assert results[0]['mail_parts'][1]['base64_encoded_payload'].startswith(
        'UEsDBBQACAAIAO')
