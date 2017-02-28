pygist
======

Extremely simple commandline interface to create Gists from files.  Generate an
[access token](https://github.com/settings/tokens/new) on Github (the only
required scope is 'gist') and replace `YOUR_TOKEN_HERE` with your token string.

### Examples

    $ pygist README.md
    ...

    $ pygist -d "Readme file for my project" README.md
    ...

    $ pygist --public README.md setup.py requirements.txt
    ...

### Specification

    usage: pygist.py [-h] [--description STR] [--public] FILE [FILE ...]

    Post file(s) to Github Gist!

    positional arguments:
      FILE               file(s) to include in the gist

    optional arguments:
      -h, --help         show this help message and exit
      --description STR  description for Gist
      --public           make Gist public
