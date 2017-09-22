import sys
import logging
import textwrap
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from pprint import pprint
import json

from csirtg_mail import parse_email_from_string

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s[%(lineno)s] - %(message)s'

logger = logging.getLogger(__name__)


def main():

    p = ArgumentParser(
        description=textwrap.dedent('''\

        csirtg-mail is a CLI tool for debugging, it allows you to easily input a email message and print out the
        py-cgmail data structure.

        example usage:
            $ cat test.eml | csirtg-mail
            $ csirtg-mail --file test.eml
        '''),
        formatter_class=RawDescriptionHelpFormatter,
        prog='csirtg-mail'
    )

    p.add_argument("-f", "--file", dest="file", help="specify email file")
    p.add_argument("-d", "--debug", help="enable debugging", action="store_true")
    p.add_argument("--urls", help="print URLS to stdout", action="store_true")

    args = p.parse_args()

    loglevel = logging.INFO
    if args.debug:
        loglevel = logging.DEBUG

    console = logging.StreamHandler()
    logging.getLogger('').setLevel(loglevel)
    console.setFormatter(logging.Formatter(LOG_FORMAT))
    logging.getLogger('').addHandler(console)

    options = vars(args)

    # get email from file or stdin
    if options.get("file"):
        with open(options["file"]) as f:
            email = f.read()
    else:
        email = sys.stdin.read()

    # parse email message
    results = parse_email_from_string(email)

    if args.urls:
        for e in results:
            for u in e['urls']:
                print(u)

        raise SystemExit

    if args.debug:
        results = json.dumps(results, indent=4)
    else:
        results = json.dumps(results)

    print(results)


if __name__ == "__main__":
    main()
