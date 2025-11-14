#!/usr/bin/python3

# v7. Dated 9th January 2021
# Strip any trailing new line characters from clipboard url.
# Limit the length of the webpage title returned to 84 characters.

# v6. Dated 22nd December 2020
# Added new function convmv, to ensure filename.url will be utf8 encoding.

# v5. Dated 23rd Nov 2020
# Add xsel clipboard support using subprocess,
# Add validus to validate clipboard.
# add colorama to make things pretty.

# v3. Dated 5th November 2020
# Added use of external module regex, for remove punctuation function.

# Added snoop debugger
# https://github.com/alexmojaki/snoop

# v2. Amended beautiful soup scraping, to include user agent info, as some
# websites would not work. HTTP_Error_403_Forbidden.
# Source for fix = 
# https://medium.com/@speedforcerun/python-crawler-http-error-403-forbidden-1623ae9ba0f

# October 2020, use beautiful soup to find url title.
# new usage example:
# create-url.py "https://theuselessweb.com/"

# October 2020, encode urlfile to ascii, to strip non ascii chars,

# create a bookmark file dot url.
# usage:
# create-url.py www.test.com "blah! blab blaj% ko^: dfsg sfsg?"

# import sys module for taking system arguments from command line

import argparse
import logging
import sys
from pathlib import Path, PosixPath

import validus
from colorama import Fore

import crurl
from crurl import converter, webscraper

# Using Handlers
logger = logging.getLogger(__name__)
# Create handlers
c_handler = logging.StreamHandler()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='A tool to generate a webpage shortcut file.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-b',
                        '--bookmark',
                        type=str,
                        help='Unformatted name for shortcut file',
                        default="")

    parser.add_argument('-w',
                        '--weblink',
                        type=str,
                        help='Weblink for shortcut',
                        default="")

    parser.add_argument('--version', action='version', version=crurl.__version__,
                        help='Print the application version and exit.')

    parser.add_argument('-v', '--verbose', action='store_const',
                        const=logging.INFO, dest='verbosity',
                        default=logging.CRITICAL,
                        help='Show all messages.')

#      parser.add_argument('-q', '--quiet', action='store_const',
                        #  const=logging.CRITICAL, dest='verbosity',
                        #  help='Show only critical errors.')
    parser.add_argument('-o', '--output', dest='output',
                        help='Where to output the generated files. If not '
                        'specified, a directory will be created, named '
                        '"output" in the current path.')

    parser.add_argument('-D', '--debug', action='store_const',
                        const=logging.DEBUG, dest='verbosity',
                        help='Show all messages, including debug messages.')

    parser.add_argument('-html', '--html', action='store_const',
                        const='html', dest='suffix',
                        default='url',
                        help='Weblink to be .html format.')

    parser.add_argument('-t',
                        '--write_test',
                        help='Create basic test.py',
                        action='store_true')

    parser.add_argument('-f',
                        '--force',
                        help='Overwrite existing bookmark if exists and use the suggested filename',
                        action='store_true')

#      parser.add_argument('--fatal', metavar='errors|warnings',
                        #  choices=('errors', 'warnings'), default='',
                        #  help=('Exit the program with non-zero status if any '
                              #  'errors/warnings encountered.'))
    return parser.parse_args()


def main():
    args = parse_arguments()

    c_handler.setLevel(args.verbosity)
    #  Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    # Add handlers to the logger
    logger.setLevel(args.verbosity)
    logger.addHandler(c_handler)

    bookmark = args.bookmark
    weblink = args.weblink
    verbosity = args.verbosity
    suffix = args.suffix


    try:

        if "".__eq__(weblink):
            logger.debug('-w argument not used.')
            #  print("weblink is empty")
            print(
            #  logging.info(
                Fore.LIGHTCYAN_EX + "\n    Reading url from clipboard...", flush=True
            )
            # Get url from clipboard
            dreg_url = converter.paste_xsel()
        else:
            logger.debug("-w argument used.")
            logger.debug(f'{args.weblink}')
            dreg_url = weblink

        # Remove trailing newlines from string dreg_url
        reg_url = dreg_url.rstrip()

        # Validate reg_url
        if not validus.isurl(reg_url):
            logger.error('No url available')
            print(
                Fore.LIGHTRED_EX + "    ⚠️   ERROR: No url available. 😢"
            )
            return

        if "".__eq__(bookmark):
            logger.debug('-b argument not used.')
            print(
                Fore.LIGHTCYAN_EX + "\n    Getting title for url...", flush=True
            )
            print(Fore.LIGHTCYAN_EX + "     ..." + reg_url, flush=True)
            dtitle = webscraper.get_title(reg_url)
        else:
            logger.debug('-b argument used.')
            logger.debug(f'{args.bookmark}')
            print(
                Fore.LIGHTCYAN_EX + "\n    Getting title for url...", flush=True
            )
            print(Fore.LIGHTCYAN_EX + "     ..." + reg_url, flush=True)
            dtitle = bookmark

        # limit length of title
        title = dtitle[0:83]

        # Strip any punctuation
        clean = converter.remove_punctuation(title)

        # Replace spaces with underscore in clean.
        spaces = converter.myreplace(" ", "_", clean)

        # Get a utf8 encoded string for the filename.
        # title from below url, has character like ö, which isn't utf8
        # https://connysoderholm.com/search-files-on-your-computer-faster-with-python
        utf8title = converter.convmv(spaces)

#          urlfile2 = (
            #  "/home/live/Dropbox/bookmarks/" + utf8title + ".url"
            #  )

        # check if file name is acceptable,
        if utf8title is not None and not args.force and not args.bookmark:
            answer = input(
                Fore.LIGHTRED_EX + f'\n Are you happy with this filename? "{utf8title}.{args.suffix}" [yN] '
            )
            if not answer.lower().startswith('y'):
                sys.exit(Fore.LIGHTGREEN_EX + '\n Rerun with the -b optional argument and define a different name. Bye!\n')

        dest_path = PosixPath(
            "~/Dropbox/bookmarks/"
        )

        #  Path.suffix = '.url'
        Path.suffix = f'.{args.suffix}'

        urlfile2 = dest_path.expanduser() / (utf8title + Path.suffix)

        # check if file name exists
        if urlfile2.is_file() and not args.force:
            answer = input(
                Fore.LIGHTRED_EX + f'\n "{urlfile2}" exists.  Overwrite? [yN] '
            )
            if not answer.lower().startswith('y'):
                sys.exit(Fore.LIGHTGREEN_EX + '\n Will not overwrite. Bye!')

        # Build the output file.

        #  converter.build_file(reg_url, urlfile2)

        if args.suffix == 'html':
            converter.build_file2(reg_url, urlfile2)
        else:
            converter.build_file(reg_url, urlfile2)
#  sys.exit(Fore.LIGHTGREEN_EX + '\n need to implement .html file creation function first. Bye!')

# Text to display.
        print(
            Fore.LIGHTYELLOW_EX + "\n    New file created at....\n"
        )
        print(
            Fore.LIGHTGREEN_EX + f"{urlfile2}\n"
        )

    except Exception as e:
        logger.critical('%s', e)

#          print(
            #  Fore.LIGHTRED_EX + f"⚠️⚠️⚠️⚠️   Error: Unexpected crash: {e}."
        #  )

        if args.verbosity == logging.DEBUG:
            raise
        else:
            sys.exit(getattr(e, 'exitcode', 1))


if __name__ == '__main__':
    main()
