import csirtg_mail

TEST_FILE = 'samples/email/single_plain_04.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'


def test_extract_urls():
    print(results[0]['urls'])
    assert "http://www.socialservices.cn:1234/detail.php?id=9" in results[0]['urls']
    assert "http://www.socialservices.cn/detail.php?id=9" in results[0]['urls']
    assert "http://user:pass@www.socialservices.cn:1234/detail.php?id=9" in results[0]['urls']
    assert "http://user:pass@www.socialservices.cn/detail.php?id=9" in results[0]['urls']
    assert "http://192.168.1.1:1234/detail.php?id=9" in results[0]['urls']
    assert "http://192.168.1.1/detail.php?id=9" in results[0]['urls']
    assert "http://user:pass@192.168.1.1:1234/detail.php?id=9" in results[0]['urls']
    assert "http://user:pass@192.168.1.1/detail.php?id=9" in results[0]['urls']
    assert "http://[2001:db8:3:4::]:1234/detail.php?id=9" in results[0]['urls']
    assert "http://[2001:db8:3:4::]/detail.php?id=9" in results[0]['urls']
    assert "http://user:pass@[2001:db8:3:4::]:1234/detail.php?id=9" in results[0]['urls']
    assert "http://user:pass@[2001:db8:3:4::]/detail.php?id=9" in results[0]['urls']
