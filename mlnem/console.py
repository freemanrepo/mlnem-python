"""
mlnem
"""

import imghdr
import argparse
import sys
import os
import config

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from pymediainfo import MediaInfo

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=FutureWarning)
    from network import image, video

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
                        help="path to image/video file")
    parser.add_argument("-u", "--url",
                        type=str, default=None,
                        help="url of a video stream to pass to the network")
    parser.add_argument("-o", "--output",
                        type=str, default=None,
                        help="write network result(s) as image/video to specified path")
    parser.add_argument("-s", "--skip-rate",
                        type=int, default=1,
                        help="Use this option to skip frames with processing video")
    parser.add_argument("-g", "--use-gpu",
                        action='store_true', default=False,
                        help="use gpu instead of cpu for processing image/video")
    parser.add_argument("-w", "--webcam",
                        action='store_true', default=False,
                        help="Use webcam as video input source")
    parser.add_argument("-V", "--version",
                        action='store_true', default=False,
                        help="show current version")
    parser.add_argument("-d", "--debug",
                        action='store_true', default=False,
                        help="set logging level to debug")
    parser.add_argument("-t", "--use-tiny",
                        action='store_true', default=False,
                        help="use tiny-yolo instead of full-yolo network")

    return parser.parse_args(args), parser

def entry():
    """
    entry
    """

    args, parser = parse_arguments(sys.argv[1:])

    if args.version:
        print('mlnem ' + config.version)
    elif args.webcam:
        video.process_video_with_path(0, use_tiny_yolo=args.use_tiny, output=args.output, use_gpu=args.use_gpu, skip_rate=args.skip_rate)
    elif args.path:
        if os.path.isfile(args.path):
            if args.output:
                if os.path.isfile(args.output):
                    print('[mlnem] file already exists at specified output path')
                    exit(1)

            if imghdr.what(args.path):
                image.process_image_with_path(args.path, use_tiny_yolo=args.use_tiny, debug_mode=args.debug, output=args.output, use_gpu=args.use_gpu)
            else:
                file_info = MediaInfo.parse(args.path)
                is_video = False
                for track in file_info.tracks:
                    if track.track_type == "Video":
                        is_video = True
                        break

                if is_video:
                    video.process_video_with_path(args.path, use_tiny_yolo=args.use_tiny, output=args.output, use_gpu=args.use_gpu, skip_rate=args.skip_rate)
                else:
                    print('[mlnem] invalid file')
        else:
            print('[mlnem] file doesn\'t exist')
    elif args.url:
        video.process_video_with_path(args.url, use_tiny_yolo=args.use_tiny, output=args.output, use_gpu=args.use_gpu, skip_rate=args.skip_rate)
    else:
        parser.print_help()
