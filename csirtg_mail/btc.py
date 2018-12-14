import re

# Regular expression for BitCoin addresses
RE_BTC = r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b'


def _extract_btcs_text(content):
    btcs = set()

    found = re.findall(RE_BTC, content, re.MULTILINE)

    for b in found:
        btcs.add(b)

    return btcs


def extract_btcs(content, html=False):
    btcs = set()

    from .constants import PYVERSION

    if PYVERSION == 3:
        content = str(content)

    if content:
        btcs = _extract_btcs_text(content)
    else:
        return btcs

    return btcs
