#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import requests


TOKEN = 'YOUR_TOKEN_HERE'
URL = 'https://api.github.com/gists'


def post_files(files, description='', public=False):
    auth_header = {'Authorization': 'token {}'.format(TOKEN)}
    data = {
        'description': description,
        'public': public,
        'files': {},
    }

    # Add files to data dict
    for fi in files:
        with open(fi) as f:
            data['files'][os.path.basename(fi)] = {'content': f.read()}

    r = requests.post(URL, headers=auth_header, json=data)

    return r.json()['html_url']


if __name__ == "__main__":
    p = argparse.ArgumentParser(description='Post file(s) to Github Gist!')
    # One or more files
    p.add_argument('files', metavar='FILE', nargs='+',
                   help='file(s) to include in the gist')
    # Description string
    p.add_argument('--description', help='description for Gist', default='',
                   metavar='STR')
    # Public flag (default private)
    p.add_argument('--public', action='store_true', help='make Gist public')

    args = p.parse_args()

    print(post_files(args.files, args.description, args.public))
