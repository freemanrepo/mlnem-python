"""
mlnem
"""

import matplotlib.pyplot as plot
import cv2
from darkflow.net.build import TFNet

import imgtools.drawer as drawer
import config

def process_image_with_path(path, debug_mode=False, output=None):
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
    imgcv = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    result = tfnet.return_predict(imgcv)

    fig, ax_obj = plot.subplots(1)
    ax_obj.imshow(imgcv)
    drawer.process_image(ax_obj, result, debug_mode=debug_mode)

    if output:
        fig.savefig(output)

    plot.show()
