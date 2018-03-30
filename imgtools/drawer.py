"""
drawer
"""

import matplotlib.patches as patches

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