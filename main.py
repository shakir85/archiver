#!/usr/bin/env python3
from app import tar
from argparse import ArgumentParser

if __name__ == '__main__':

    parser = ArgumentParser(prog='PROG', description='''Lightweight archiving tool''')

    parser.add_argument('--archive', required=True, action='store_true', help='tar a directory')
    parser.add_argument('-s', '--src', required=True, help='Absolute path to source directory. No trailing forward-slash')
    parser.add_argument('-d', '--dst', required=False, help='Absolute path to destination. No trailing forward-slash')
    parser.add_argument('-n', '--jobname', help="Task name, use any meaningful name")
    parser.add_argument('--dry-run', required=False, action='store_true')

    args = parser.parse_args()

    if args.archive:
        tar.compress_to_dest(src=args.src, dst=args.dst, job_name=args.jobname, dry_run=args.dry_run)
