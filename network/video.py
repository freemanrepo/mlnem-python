"""
mlnem
"""

import cv2
from darkflow.net.build import TFNet

import imgtools.drawer as drawer
import config

def process_video_with_path(path):
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

    while cap.isOpened():
        _, frame = cap.read()
        imgcv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = tfnet.return_predict(imgcv)
        drawer.process_video(imgcv, result)
        cv2.imshow('frame', cv2.cvtColor(imgcv, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
