import csirtg_mail

TEST_FILE = 'samples/email/single_html_02.eml'

with open(TEST_FILE) as f:
    email = f.read()

results = csirtg_mail.parse_email_from_string(email)


def test_message_headers():
    assert results[0]['headers']['return-path'][0] == 'Appidms@tripadvisor.com'


def test_message_parts():
    assert results[0]['mail_parts'][0]['decoded_body'].startswith('<HTML>\n<div id=":219" class="zz J-J5-Ji">')


def test_extract_urls():
    assert "http://www.homerunsports.com/sites/all/themes/zen/zen-internals/css/direct/index.php?cmd=_login-processing&login_cmd=_login-done&login_access=852105208512140" in results[0]['urls']

