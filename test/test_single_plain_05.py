import csirtg_mail

TEST_FILE = 'samples/email/single_plain_05.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email, defanged_urls=True)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'


def test_extract_urls():
    print(results[0]['urls'])
    assert "hxxp://www.blah.blah.com.badness.com/wp=stuff/uno/dos/tres/" in results[0]['urls']
