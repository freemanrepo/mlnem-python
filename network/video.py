"""
mlnem
"""

import cv2
from darkflow.net.build import TFNet

import imgtools.drawer as drawer
import config

def process_video_with_path(path, output=None):
    """
    process_with_path
    """

    options = {}
    options['threshold'] = 0.1

    if config.usesTinyNetwork:
        print('[mlnem] configuring network using tiny-yolo')
        options['pbLoad'] = config.__dir__ + '/bin/tiny-yolo.pb'
        options['metaLoad'] = config.__dir__ + '/bin/tiny-yolo.meta'
    else:
        print('[mlnem] configuring network using yolo')
        options['pbLoad'] = config.__dir__ + '/bin/yolo.pb'
        options['metaLoad'] = config.__dir__ + '/bin/yolo.meta'

    tfnet = TFNet(options)

    cap = cv2.VideoCapture(path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    cv2.namedWindow('frame', 0)
    cv2.resizeWindow('frame', int(width / 2), int(height / 2))

    if output:
        out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            imgcv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            drawer.process_video(imgcv, tfnet.return_predict(imgcv))
            colored = cv2.cvtColor(imgcv, cv2.COLOR_BGR2RGB)

            if output:
                out.write(colored)

            cv2.imshow('frame', colored)

            if cv2.waitKey(fps) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    if output:
        out.release()
    cv2.destroyAllWindows()
