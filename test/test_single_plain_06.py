import csirtg_mail

TEST_FILE = 'samples/email/single_plain_06.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email, defanged_urls=True)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'


def test_extract_btcs():
    print(results[0]['btcs'])
    assert "1KhDTLk95fZQBd5tUXj4123459bBAji2DB" in results[0]['btcs']
