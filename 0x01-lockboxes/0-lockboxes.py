#!/usr/bin/python3
'''Description: A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''
    This function checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    :param boxes: List of lists... each inner list represents a box,
                  and the indices in the inner list are the keys to other boxes.
    :type boxes: List of lists

    :return: True if all boxes can be unlocked, False otherwise.
    :rtype: bool
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
