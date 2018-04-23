"""
drawer
"""

import matplotlib.patches as patches
import cv2
import config

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
            rect = patches.Rectangle((topleft['x'], topleft['y']), bottomright['x'] - topleft['x'], bottomright['y'] - topleft['y'], linewidth=4, edgecolor='r', facecolor='none')
            ax_obj.text(topleft['x'], topleft['y'], result['label'], verticalalignment='bottom', horizontalalignment='left', color='black', fontsize=6, clip_on=True, bbox=dict(facecolor='r', edgecolor='r', pad=0.0))
            ax_obj.add_patch(rect)

def process_video(img_cv, network_results=None, debug_mode=False):
    """
    process_video
    """

    if network_results != None or not network_results:
        found_person = False

        for result in network_results:
            if result['confidence'] < 0.4:
                if debug_mode:
                    print('[mlnem] skipping ' + result['label'] + ' with low confidence: ' +
                          str('{0:.2f}'.format(result['confidence'] * 100)) + '%')
                continue

            if result['label'] == 'person':
                found_person = True

            if debug_mode:
                print('[mlnem] found a ' + result['label'] + ' with ' +
                      str('{0:.2f}'.format(result['confidence'] * 100)) + '% confidence!')

            topleft = result['topleft']
            bottomright = result['bottomright']

            color = config.colors[result['label']]

            if color is None:
                color = (255, 0, 0)

            cv2.rectangle(img_cv, (topleft['x'], topleft['y']), (bottomright['x'], bottomright['y']), color, 4)
            cv2.putText(img_cv, result['label'], (topleft['x'], topleft['y'] - 6), 0, 0.6, color, 2)

        return found_person

    return False
