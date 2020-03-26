"""PW CLI

Has a dependency on the app xsel being installed
install with:
	sudo apt install xsel

Usage:
pw.py [--size=<sz>] [--copy]
pw.py -h|--help
pw.py -v|--version

Options:
--copy  automatically copy newly created password to the clipboard
-h --help  Show this screen.
-v --version  Show version.
"""
from docopt import docopt
from random import choice
from subprocess import Popen, PIPE


def mkpassword(psize):
    pwd = []
    charsets = [
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789',
        '^!\$%&/()=?{[]}+~#-_.:,;<>|\\',
    ]
    charset = choice(charsets)
    while len(pwd) < psize:
        pwd.append(choice(charset))
        charset = choice(list(set(charsets) - set([charset])))
    return "".join(pwd)


def paste(str):

    p = Popen(['xsel', '-bi'], stdin=PIPE)
    p.communicate(input=str)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='pw 0.0.1a')

    size = arguments.get('--size')
    clip = arguments.get('--copy')

    if size is None:
        # default the password size if no length passed in
        size = 12

    x = mkpassword(psize=int(size))
    print(x)

    if clip is True:
    	paste(x)
