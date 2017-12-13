import csirtg_mail
from pprint import pprint

TEST_FILE = 'samples/email/multi_mixed_msdoc.eml'

with open(TEST_FILE) as f:
    email = f.read()


def test_mytest():
    results = csirtg_mail.from_string(email)
    assert results['attachments'][0]['type'] == 'application/msword'


if __name__ == "__main__":
    test_mytest()