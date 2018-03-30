"""
mlnem
"""

import imghdr
import argparse
import sys
import os
import config

from network import image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def parse_arguments(args):
    """Parse the command line arguments for the console commands.
    Args:
      args (List[str]): List of string arguments to be parsed.
    Returns:
      Namespace: Namespace with the parsed arguments.
      ArgumentParser: Parser object
    """

    parser = argparse.ArgumentParser(
        description="yolo network implementation in a ready-to-use python app."
    )

    parser.add_argument("-p", "--path",
                        type=str, default=None,
                        help="Path to image/video file.")
    parser.add_argument("-V", "--version",
                        action='store_true', default=False,
                        help="Show current version.")
    parser.add_argument("-d", "--debug",
                        action='store_true', default=False,
                        help="Set logging level to debug.")

    return parser.parse_args(args), parser

def entry():
    """
    entry
    """

    args, parser = parse_arguments(sys.argv[1:])

    if args.version:
        print('mlnem ' + config.version)
    elif args.path:
        if os.path.isfile(args.path):
            if imghdr.what(args.path):
                image.process_with_path(args.path, debug_mode=args.debug)
            else:
                print('[mlnem] invalid image file')
        else:
            print('[mlnem] file doesn\'t exist')
    else:
        parser.print_help()
