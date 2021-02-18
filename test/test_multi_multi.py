import csirtg_mail
from pprint import pprint

TEST_FILE = 'samples/email/Test_multipart.eml'

with open(TEST_FILE, encoding='utf8') as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'
    assert results[1]['headers']['return-path'][0] == '<john@csirtgadgets.org>'
    assert results[2]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'
    assert results[3]['headers']['return-path'][0] == '<john@csirtgadgets.org>'
    assert results[4]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'
    assert results[5]['headers']['return-path'][0] == '<advertisebz09ua@gmail.com>'
    assert results[6]['headers']['return-path'][0] == '<bob@example.com>'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith(
        'Hello,\nBoost your Facebook')
    assert results[1]['mail_parts'][0]['decoded_body'].startswith(
        'http://www.indiana.edu\n\nJohn\n')
    assert results[2]['mail_parts'][0]['decoded_body'].startswith(
        'Hello,\nBoost your Facebook posts with a massive')
    assert results[3]['mail_parts'][0]['decoded_body'].startswith(
        'Hello friend,\n\nMy name is Miss Ammaarah Younis from Libya. ')
    assert results[4]['mail_parts'][0]['decoded_body'].startswith(
        '\nPlease find the details of the following new Phishing ')
    assert results[5]['mail_parts'][0]['decoded_body'].startswith(
        'You may not know me and you are probably wondering why')
    assert results[6]['mail_parts'][0]['decoded_body'].startswith(
        'This is a test of multiple attachments\n')


def test_extract_urls():
    assert 'http://www.socialservices.cn/detail.php?id=9' in results[0]['urls']

    assert 'http://www.indiana.edu' in results[1]['urls']

    assert 'http://user:pass@www.socialservices.cn:1234/detail.php?id=9' in results[2]['urls']
    assert 'http://user:pass@192.168.1.1/detail.php?id=9' in results[2]['urls']
    assert 'http://user:pass@[2001:db8:3:4::]/detail.php?id=9' in results[2]['urls']
    assert 'http://user:pass@www.socialservices.cn/detail.php?id=9' in results[2]['urls']
    assert 'http://192.168.1.1:1234/detail.php?id=9' in results[2]['urls']
    assert 'http://user:pass@[2001:db8:3:4::]:1234/detail.php?id=9' in results[2]['urls']
    assert 'http://user:pass@192.168.1.1:1234/detail.php?id=9' in results[2]['urls']
    assert 'http://[2001:db8:3:4::]/detail.php?id=9' in results[2]['urls']
    assert 'http://www.socialservices.cn:1234/detail.php?id=9' in results[2]['urls']
    assert 'http://[2001:db8:3:4::]:1234/detail.php?id=9' in results[2]['urls']
    assert 'http://192.168.1.1/detail.php?id=9' in results[2]['urls']
    assert 'http://www.socialservices.cn/detail.php?id=9' in results[2]['urls']

    assert [] == results[3]['urls']
    assert [] == results[4]['urls']
    assert [] == results[5]['urls']
    assert [] == results[6]['urls']


def test_extract_emails():

    assert [] == results[0]['body_email_addresses']
    assert [] == results[1]['body_email_addresses']

    assert 'pass@192.168.1.1' in results[2]['body_email_addresses']
    assert 'pass@www.socialservices.cn' in results[2]['body_email_addresses']

    assert 'yyounisammaarah2015@gmail.com' in results[3]['body_email_addresses']

    assert [] == results[4]['body_email_addresses']
    assert [] == results[5]['body_email_addresses']
    assert [] == results[6]['body_email_addresses']
