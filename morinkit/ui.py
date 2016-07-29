# -*- coding: ascii -*-

"""
morinkit.ui
~~~~~~~~~~~

This module defines the CLI for calling various top-level functions.
"""

import sys
from argparse import ArgumentParser, FileType


def parse_args():
    """Parse command-line arguments.

    Returns:
        A dict containing the subcommand and all other positional and
        optional arguments.
    """
    # Initialize parser and subparsers
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand')

    # calc_strelka_vaf
    calc_strelka_vaf = subparsers.add_parser('calc_strelka_vaf')
    calc_strelka_vaf.add_argument('vcf_files', nargs='+', metavar='vcf_file')
    calc_strelka_vaf.add_argument('--output', '-o', default='/dev/stdout')

    # Parse arguments and return dict
    args = parser.parse_args()
    return vars(args)
