#!/usr/bin/env python3
from app import tar
from argparse import ArgumentParser


def arguments():
    parser = ArgumentParser(prog='PROG', description='''Lightweight archiving tool''')
    parser.add_argument('--archive', required=True, action='store_true', help='tar a directory')
    parser.add_argument('-s', '--src', required=True, help='Absolute path to source directory. No trailing slash')
    parser.add_argument('-d', '--dst', required=False, help='Absolute path to destination. No trailing slash')
    parser.add_argument('-n', '--jobname', help="Task name, use any meaningful name")
    parser.add_argument('--dry-run', required=False, action='store_true')

    return parser.parse_args()


def remove_trail_slash(path):
    if path.endswith('/'):
        path = path[:-1]
    return path


if __name__ == '__main__':

    args = arguments()
    src = remove_trail_slash(args.src)
    dst = remove_trail_slash(args.dst)

    if args.archive:
        tar.compress_to_dest(src=src, dst=dst, job_name=args.jobname, dry_run=args.dry_run)
