import csirtg_mail

TEST_FILE = 'samples/email/single_plain_01.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith('Hello')


def test_extract_urls():
    assert "http://www.socialservices.cn/detail.php?id=9" in results[0]['urls']

