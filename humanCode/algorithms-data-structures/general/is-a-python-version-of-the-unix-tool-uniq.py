#!/usr/bin/env python3
"""
A recreation of the POSIX uniq tool.
"""

import collections
import enum
import itertools
import re
import sys
import functools

UniqMode = enum.Enum(
    "UniqMode",
    [
        "normal",
        "count",
        "suppress_repeated",
        "suppress_not_repeated",
    ],
)
UniqMode.__doc__ = """
UniqMode enumerates the different modes that the script can
run in.

- UniqMode.normal is the default mode.
- UniqMode.count corresponds to the "-c" flag.
- UniqMode.suppress_repeated corresponds to the "-u" flag.
- UniqMode.suppress_not_repeated corresponds to the "-d"
  flag.
"""


def run(*, mode, input_file, output_file, fields, char):
    """Run the uniq script.
    
    mode -- the UniqMode of the script.
    input_file -- read lines from this file.
    output_file -- output information to this file.
    fields -- the number of fields to skip.
    char -- the number of characters to skip after fields.

    """
    lines = map(remove_newline, input_file)
    line_key = functools.partial(
        preprocess_line, fields=fields, char=char
    )

    for _, duplicates in itertools.groupby(lines, line_key):
        duplicates = tuple(duplicates)

        repeated = len(duplicates) > 1
        if mode is UniqMode.suppress_repeated and repeated:
            continue
        if (
            mode is UniqMode.suppress_not_repeated
            and not repeated
        ):
            continue

        if mode is UniqMode.count:
            message = f"{len(duplicates)} {duplicates[0]}"
        else:
            message = f"{duplicates[0]}"

        print(message, file=output_file)


def preprocess_line(line, *, fields, char):
    """Preprocess a line by removing initial fields and
    characters.

    fields -- the number of fields to remove.
    char -- the number of characters to remove after the
            fields.

    """
    if fields > 0:
        line = re.sub(r"\s*\S*", "", line, count=fields)
    line = line[char:]
    return line


def remove_newline(text):
    """Remove a trailing newline from text."""
    if text.endswith("\n"):
        text = text[:-1]
    return text


def positive_integer(text):
    """Parse a positive integer from text.

    Raises an Exception for bad text.
    """
    n = int(text)
    if n <= 0:
        raise ValueError()
    return n


def input_FileType(filename):
    """Like argparse.FileType("r") but the filename "-" is
    turned into sys.stdin.
    """
    if filename == "-":
        return sys.stdin
    else:
        return open(filename, "r")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="report or filter out repeated lines in a file",
        prefix_chars="-+",
    )
    parser.set_defaults(mode=UniqMode.normal)
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "-c",
        "+c",
        help="""
        Precede each output line with a count of the number
        of times the line occurred in the input.
        """,
        action="store_const",
        const=UniqMode.count,
        dest="mode",
    )
    mode_group.add_argument(
        "-d",
        "+d",
        help="""
        Suppress the writing of lines that are not repeated
        in the input.
        """,
        action="store_const",
        const=UniqMode.suppress_not_repeated,
        dest="mode",
    )
    mode_group.add_argument(
        "-u",
        "+u",
        help="""
        Suppress the writing of lines that are repeated in
        the input.
        """,
        action="store_const",
        const=UniqMode.suppress_repeated,
        dest="mode",
    )
    parser.add_argument(
        "-f",
        "+f",
        metavar="fields",
        type=positive_integer,
        help="""
        Ignore the first fields fields on each input line
        when doing comparisons, where fields is a positive
        decimal integer. A field is the maximal string
        matched by the basic regular expression:
        /[[:blank:]]*[^[:blank:]]*/. If the fields
        option-argument specifies more fields than appear on
        an input line, a null string shall be used for
        comparison.
        """,
        default=0,
    )
    parser.add_argument(
        "-s",
        "+s",
        metavar="char",
        type=positive_integer,
        help="""
        Ignore the first chars characters when doing
        comparisons, where chars shall be a positive decimal
        integer. If specified in conjunction with the -f
        option, the first chars characters after the first
        fields fields shall be ignored. If the chars
        option-argument specifies more characters than
        remain on an input line, a null string shall be used
        for comparison.
        """,
        default=0,
    )
    parser.add_argument(
        "input_file",
        help="""
        A pathname of the input file. If the input_file
        operand is not specified, or if the input_file is
        '-', the standard input shall be used.
        """,
        nargs="?",
        type=input_FileType,
        default=sys.stdin,
    )
    parser.add_argument(
        "output_file",
        help="""
        A pathname of the output file. If the output_file
        operand is not specified, the standard output shall
        be used. The results are unspecified if the file
        named by output_file is the file named by
        input_file.
        """,
        nargs="?",
        type=argparse.FileType("w"),
        default=sys.stdout,
    )
    args = parser.parse_args()

    with args.input_file, args.output_file:
        run(
            mode=args.mode,
            input_file=args.input_file,
            output_file=args.output_file,
            fields=args.f,
            char=args.s,
        )
