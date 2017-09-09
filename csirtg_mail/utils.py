import pyzmail
import re

# https://stackoverflow.com/questions/2168719/parsing-forwarded-emails
# https://github.com/zapier/email-reply-parser
# https://en.wikipedia.org/wiki/Email_forwarding
# https://en.wikipedia.org/wiki/List_of_email_subject_abbreviations

RE_FWD = re.compile('\^(FWD?|Fwd?):')


def parse_headers(message):
    keys = message.keys()
    values = message.values()
    headers = {}

    for k, v in zip(keys, values):
        headers.setdefault(k.lower(), []).append(v)

    return headers


def is_redirect(message):
    assert isinstance(message, pyzmail.PyzMessage)

    headers = parse_headers(message)

    if headers['resent-to'][0]:
        return True

    if headers['x-envelope-to'][0]:
        return True

    return False


def is_fwd(message):
    assert isinstance(message, pyzmail.PyzMessage)

    headers = parse_headers(message)

    if RE_FWD.match(headers['subject'][0]):
        return True

    if headers.get('x-forwarded-message-id'):
        return True

    # no subject, but attachment
    ## either .eml or [.docx?|.zip|.html?]

    return is_redirect(message)

