import re
import socket
from bs4 import BeautifulSoup
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

from pprint import pprint

RE_URL_PLAIN = r'(https?://[^\s>|^\"]+)'
RE_URL_DEFANGED = r'((?:hxxps?:\/\/.*?(?=\/))(?:.*?(?=\s)))'
RE_IPV4 = re.compile(
    '^(.+:.+@)?(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(:\d+)?$')
# http://stackoverflow.com/a/17871737
RE_IPV6 = re.compile('^(.+:.+@)?\[?(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\]?(:\d+)?$')
# http://goo.gl/Cztyn2 -- probably needs more work
RE_FQDN = re.compile(
    '^(.+:.+@)?((xn--)?(--)?[a-zA-Z0-9-_]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}(--p1ai)?(:\d+)?$')
RE_URI_SCHEMES = re.compile('^(https?|hxxps?|ftp)$')
RE_EMAIL_ADDRESS = re.compile(
    '(?:%\w\w)?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')


def _extract_email_addresses_text(content):
    email_addresses = set()

    from .constants import PYVERSION

    if PYVERSION == 3:
        content = str(content)

    found = re.findall(RE_EMAIL_ADDRESS, content)

    for address in found:
        email_addresses.add(address)

    return email_addresses


def _extract_email_addresses_html(content):
    email_addresses = set()

    from .constants import PYVERSION

    if PYVERSION == 3:
        content = str(content)

    soup = BeautifulSoup(content, "lxml")

    # Look in anchor links for email addresses - common with mailto:
    for link in soup.find_all("a"):
        found = re.findall(
            RE_EMAIL_ADDRESS, str(link))
        for address in found:
            email_addresses.add(address)

    # look in the text of the email
    found = re.findall(
        RE_EMAIL_ADDRESS, soup.get_text(separator=' '))

    for address in found:
        email_addresses.add(address)

    return email_addresses


def extract_email_addresses(content, html=False):
    email_addresses = set()

    if content:
        if html:
            email_addresses = _extract_email_addresses_html(content)
        else:
            email_addresses = _extract_email_addresses_text(content)
    else:
        return email_addresses

    return email_addresses


def _url(s):
    u = urlparse(s)
    if re.match(RE_URI_SCHEMES, u.scheme):
        if _fqdn(u.netloc) or _ipv4(u.netloc) or _ipv6(u.netloc):
            return True


def _ipv6(s):
    try:
        socket.inet_pton(socket.AF_INET6, s)
    except socket.error:
        if not re.match(RE_IPV6, s):
            return False

    return True


def _ipv4(s):
    try:
        socket.inet_pton(socket.AF_INET, s)
    except socket.error:
        if not re.match(RE_IPV4, s):
            return False
    return True


def _fqdn(s):
    if RE_FQDN.match(s):
        return 1


def url_to_fqdn(s):
    u = urlparse(s)
    if re.match(RE_URI_SCHEMES, u.scheme):
        if _fqdn(u.netloc):
            return u.netloc


def _extract_urls_text(content, defanged_urls=False):
    urls = set()

    found = re.findall(RE_URL_PLAIN, content, re.MULTILINE)
    if defanged_urls:
        found = re.findall(RE_URL_DEFANGED, content) + \
            re.findall(RE_URL_PLAIN, content, re.MULTILINE)

    for u in found:
        u = u.replace(" ", "")
        if defanged_urls:
            urls.add(u)
        else:
            if _url(u):
                urls.add(u)

    return urls


def _extract_urls_html(body, defanged_urls=False, images=False):
    urls = set()
    soup = BeautifulSoup(body, "lxml")

    for link in soup.find_all('a'):
        if link.get('href'):
            if _url(link.get('href')):
                urls.add(link.get('href'))

    if not images:
        return urls

    for link in soup.find_all('img'):
        if link.get('src'):
            if _url(link.get('src')):
                urls.add(link.get('src'))

    return urls


def extract_urls(content, html=False, defanged_urls=False, sanitize_urls=False):
    urls = set()

    from .constants import PYVERSION

    if PYVERSION == 3:
        content = str(content)

    if content:
        if html:
            urls = _extract_urls_html(content, defanged_urls=defanged_urls)
        else:
            urls = _extract_urls_text(content, defanged_urls=defanged_urls)

        # check do we want to strip parameters from URLs, i.e. remove '?foo=bar'
        if sanitize_urls:
            sanitized_urls = set()
            for url in urls:
                if '?' in url: # if this URL has parameters
                    param_start = url.index('?')
                    s_url = url[:param_start]
                    sanitized_urls.add(s_url) # Add the sanitized URL to the sanitized set
            urls = sanitized_urls # replace the set we are returning with the sanitized set
    else:
        return urls

    return urls
