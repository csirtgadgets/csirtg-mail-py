import csirtg_mail
from csirtg_mail.constants import PYVERSION

TEST_FILE = 'samples/email/single_html_05.eml'

if PYVERSION > 2:
    with open(TEST_FILE, encoding='latin-1') as f:
        email = f.read()
        email = str(email)
else:
    with open(TEST_FILE) as f:
        email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'


def test_body_email_addresses():
    assert "user1@example.com" in results[0]['body_email_addresses']
    assert "user2@example.com" in results[0]['body_email_addresses']
