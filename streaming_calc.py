#!/usr/bin/env python3
# coding: utf-8

"""Bandwidth calculation for streaming server."""

from argparse import ArgumentParser
from sys import argv, exit


def bw_server(args_bw_server):
    """Determine necessary server bandwidth."""
    sum_bw_server = \
        125 * args_bw_server.nblisteners * args_bw_server.bitrate / 128
    print(f"""Number of listeners: {args_bw_server.nblisteners}
Bitrate (kb/s): {args_bw_server.bitrate}
Server bandwidth (Mib/s): {sum_bw_server}""")


def server_usage_bw(args_server_usage_bw):
    """Determine the amount of data used for the streaming."""
    sum_server_usage_bw = \
        28125 * args_server_usage_bw.nbdays * args_server_usage_bw.nbhours * \
        args_server_usage_bw.bitrate * \
        args_server_usage_bw.nblisteners / 65536
    print(f"""Number of listeners: {args_server_usage_bw.nblisteners}
Bitrate (kb/s): {args_server_usage_bw.bitrate}
Number of days: {args_server_usage_bw.nbdays}
Number of hours by days: {args_server_usage_bw.nbhours}
Bandwidth used (GiB): {sum_server_usage_bw}""")


def main():
    """Main function with parsing arguments."""
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_bwserver = subparsers.add_parser(
        'bwserver',
        help='Determine necessary server bandwidth'
    )
    parser_bwserver.add_argument(
        'nblisteners',
        type=float,
        help='number of listeners'
    )
    parser_bwserver.add_argument(
        'bitrate',
        type=float,
        help='bitrate in kb/s'
    )
    parser_bwserver.set_defaults(func=bw_server)

    parser_serverusagebw = subparsers.add_parser(
        'usagebw',
        help='Determine the amount of data used for the streaming'
    )
    parser_serverusagebw.add_argument(
        'nblisteners',
        type=float,
        help='number of listeners')
    parser_serverusagebw.add_argument(
        'bitrate',
        type=float,
        help='bitrate in kb/s')
    parser_serverusagebw.add_argument(
        'nbdays',
        type=float,
        help='number of days')
    parser_serverusagebw.add_argument(
        'nbhours',
        type=float,
        help='number of hours by days (integer only)')
    parser_serverusagebw.set_defaults(func=server_usage_bw)

    args = parser.parse_args()
    if len(argv) == 1:
        parser.print_help()
        exit(1)
    args.func(args)


if __name__ == '__main__':
    main()
