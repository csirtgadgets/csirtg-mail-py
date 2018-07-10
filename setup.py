import os
from setuptools import setup, find_packages
import versioneer
import sys

# vagrant doesn't appreciate hard-linking
if os.environ.get('USER') == 'vagrant' or os.path.isdir('/vagrant'):
    del os.link

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

# https://www.pydanny.com/python-dot-py-tricks.html
if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'coverage',
        'pytest_cov',
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirments." % err_msg
        raise ImportError(msg)
    r = os.system('pytest test -v --cov=csirtg_mail --cov-fail-under=50')
    if r == 0:
        sys.exit()
    else:
        raise RuntimeError('tests failed')

cmds = [
    'csirtg-mail=csirtg_mail.client:main'
]

setup(
    name="csirtg_mail",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="the fastest way to parse mail",
    long_description="the fastest way to parse mail",
    url="https://github.com/csirtgadgets/csirtg-mail-py",
    license='MPL2',
    classifiers=[
               "Topic :: System :: Networking",
               "Environment :: Other Environment",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
               "Programming Language :: Python",
               ],
    keywords=['security'],
    author="Wes Young",
    author_email="wes@csirtgadgets.org",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'pyzmail',
        'chardet',
        'lxml',
        'html5lib'
    ],
    entry_points={
        'console_scripts': cmds
    },
)
