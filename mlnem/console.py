"""
mlnem
"""

import imghdr
import argparse
import sys
import os
import config

from pymediainfo import MediaInfo
from network import image, video

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
                        help="Path to image/video file")
    parser.add_argument("-V", "--version",
                        action='store_true', default=False,
                        help="Show current version")
    parser.add_argument("-d", "--debug",
                        action='store_true', default=False,
                        help="Set logging level to debug")
    parser.add_argument("-o", "--output",
                        type=str, default=None,
                        help="Write network result as image/video to specified output path")

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
            if args.output:
                if os.path.isfile(args.output):
                    print('[mlnem] file already exists at specified output path')
                    exit(1)

            if imghdr.what(args.path):
                image.process_image_with_path(args.path, debug_mode=args.debug, output=args.output)
            else:
                file_info = MediaInfo.parse(args.path)
                is_video = False
                for track in file_info.tracks:
                    if track.track_type == "Video":
                        is_video = True
                        break

                if is_video:
                    video.process_video_with_path(args.path, output=args.output)
                else:
                    print('[mlnem] invalid file')
        else:
            print('[mlnem] file doesn\'t exist')
    else:
        parser.print_help()
