"""
drawer
"""

import matplotlib.patches as patches
import cv2

def process_image(ax_obj, network_results=None, debug_mode=False):
    """
    process_image
    """

    if network_results != None:
        for result in network_results:
            if result['confidence'] < 0.4:
                if debug_mode:
                    print('[mlnem] skipping ' + result['label'] + ' with low confidence: ' +
                          str('{0:.2f}'.format(result['confidence'] * 100)) + '%')
                continue

            if debug_mode:
                print('[mlnem] found a ' + result['label'] + ' with ' +
                      str('{0:.2f}'.format(result['confidence'] * 100)) + '% confidence!')

            topleft = result['topleft']
            bottomright = result['bottomright']
            rect = patches.Rectangle((topleft['x'], topleft['y']), bottomright['x'] - topleft['x'], bottomright['y'] - topleft['y'], linewidth=1, edgecolor='r', facecolor='none')
            ax_obj.text(topleft['x'], topleft['y'], result['label'], verticalalignment='bottom', horizontalalignment='left', color='black', fontsize=6, clip_on=True, bbox=dict(facecolor='r', edgecolor='r', pad=0.0))
            ax_obj.add_patch(rect)

def process_video(img_cv, network_results=None, debug_mode=False):
    """
    process_video
    """

    if network_results != None or len(network_results) == 0:
        for result in network_results:
            if result['confidence'] < 0.4:
                if debug_mode:
                    print('[mlnem] skipping ' + result['label'] + ' with low confidence: ' +
                          str('{0:.2f}'.format(result['confidence'] * 100)) + '%')
                continue

            if debug_mode:
                print('[mlnem] found a ' + result['label'] + ' with ' +
                      str('{0:.2f}'.format(result['confidence'] * 100)) + '% confidence!')

            topleft = result['topleft']
            bottomright = result['bottomright']

            cv2.rectangle(img_cv, (topleft['x'], topleft['y']), (bottomright['x'], bottomright['y']), (255,0,0), 1)
            size, _ = cv2.getTextSize(result['label'], 0, 0.5, 1)
            cv2.rectangle(img_cv, (topleft['x'], topleft['y'] - size[1] - 6), (topleft['x'] + size[0], topleft['y']), (255,0,0), cv2.FILLED)
            cv2.putText(img_cv, result['label'], (topleft['x'], topleft['y'] - 6), 0, 0.5, (0, 0, 0), 1)
