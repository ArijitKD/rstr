#!/usr/bin/env python3

# File: ./rstr.py
#
# rstr - Generate a cryptographically secure random ASCII string of a given length
# using the system's random bytes generator.
#
#
# Copyright (C) 2025-Present Arijit Kumar Das <arijitkdgit.official@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import sys
import os

DEFAULT_RSTR_CFG = {
    "length"  : 16,
    "digit"   : True,
    "ucase"   : True,
    "lcase"   : True,
    "special" : True
}

VALID_ARGS = {
    "--help",    "-h",
    "--version", "-v",
    "--digit",   "-d",
    "--ucase",   "-u",
    "--lcase",   "-l",
    "--special", "-s"
}

VERSION = "1.0"

RNDBLK_SIZE = 512

CHAR_LCASE   = [chr(x) for x in range(97, 123)]
CHAR_UCASE   = [chr(x) for x in range(65, 91)]
CHAR_DIGIT   = [chr(x) for x in range(48, 58)]
CHAR_SPECIAL = [chr(x) for x in range(33, 48)]

HELP_TEXT = \
f'''Help for rstr (version: {VERSION})
'''\
'''
rstr: Generate a cryptographically secure random ASCII string of a given length
using the system's random bytes generator.

#1 Possible usage patterns:
  1. rstr [<string-length>] [{-u | --ucase}] [{-l | --lcase}] \\
          [{-d | --digit}] [{-s | --special}]
  2. rstr {-h | --help}
  3. rstr {-v | --version}

#2 Meanings of notations used above:
  - <...>         :  A mandatory value that must not contain a space anywhere.
  - {... | ...}   :  A shorthand and full name for the same option.
  - [...]         :  Non-mandatory options.
'''\
f'''
#3 Available options:
  1. -u, --ucase :   Specify whether to include upper case ASCII characters.
  2. -l, --lcase :   Specify whether to include lower case ASCII characters.
  3. -d, --digit :   Specify whether to include ASCII digits.
  4. -s, --special : Specify whether to include special characters.
                     
#4 Points to be noted:
  - If none of the options are specified, including the length, then the
    generated string has 16 characters and may contain all of upper case,
    lower case, digit or special ASCII characters.

  - If the length is specified, but none of the other options are specified,
    then the generated string has the specified length and contains a mix of
    all three types of ASCII characters as mentioned in the previous point.

  - Irrespective of whether the length is specified or not, if at least one
    of the 4 available options from section #3 is specified, all other options
    except the one(s) specified will be excluded from the generated string.

  - Special characters include only these:
    {CHAR_SPECIAL}.
'''

VERSION_TEXT = \
f'''rstr {VERSION}
Copyright (c) 2025-Present Arijit Kumar Das <arijitkdgit.official@gmail.com>
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This program is free software; you may redistribute it under the terms of
the GNU General Public License version 3 or later.
This program has absolutely no warranty.'''


def get_args() -> dict:
    args: list = sys.argv[1:]
    rstr_cfg: dict = DEFAULT_RSTR_CFG.copy()

    if (args == []):
        return rstr_cfg

    if (args[0] in {"--help", "-h"}):
        return {"help" : True}

    if (args[0] in {"--version", "-v"}):
        return {"version" : True}

    if (args[0].isdigit() and len(args) == 1):
        rstr_cfg["length"] = int(args[0])
        return rstr_cfg

    rstr_cfg["digit"] = False
    rstr_cfg["ucase"] = False
    rstr_cfg["lcase"] = False
    rstr_cfg["special"] = False

    for arg in args:
        if (args.index(arg) == 0 and arg.isdigit()):
            rstr_cfg["length"] = int(arg)

        elif (arg in {"--digit", "-d"}):
            rstr_cfg["digit"] = True

        elif (arg in {"--ucase", "-u"}):
            rstr_cfg["ucase"] = True

        elif (arg in {"--lcase", "-l"}):
            rstr_cfg["lcase"] = True

        elif (arg in {"--special", "-s"}):
            rstr_cfg["special"] = True

        else:
            return {}

    return rstr_cfg


def main():
    parsed_args: dict = get_args()

    if (parsed_args == {}):
        print(
            "rstr: Invalid arguments or combination of arguments.\n"
            "Use \"rstr -h\" to view help."
        )
        sys.exit(1)

    if ("help" in parsed_args):
        print (HELP_TEXT)
        sys.exit(0)

    if ("version" in parsed_args):
        print (VERSION_TEXT)
        sys.exit(0)

    rstr: str = ""
    while (len(rstr) < parsed_args["length"]):
        rand_bytes: bytes = os.urandom(RNDBLK_SIZE)
        for byte in rand_bytes:
            if (len(rstr) >= parsed_args["length"]):
                break
            char: str = chr(byte)
            if ((char in CHAR_LCASE and parsed_args["lcase"]) or
                (char in CHAR_UCASE and parsed_args["ucase"]) or
                (char in CHAR_DIGIT and parsed_args["digit"]) or
                (char in CHAR_SPECIAL and parsed_args["special"])):
                rstr += char

    print (rstr)
    sys.exit(0)

if (__name__ == "__main__"):
    main()

