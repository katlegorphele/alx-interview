#!/usr/bin/env python3

'''
Method that determines if all boxes can be opened
'''

from typing import List

def canUnlockAll(boxes: List[list]) -> bool:
    '''Check if all boxes can be unlocked'''

    unlocked = {}

    try:
        empty_index = boxes.index([])
        boxes[empty_index] = [0]
    except Exception:
        pass

    box_num = [x for x in range(len(boxes))]

    unlocked[0] = 'unlocked'
    for i in range(len(boxes) - 1):
        for k in range(len(boxes[i])):
            if boxes[i][k] in box_num:
                unlocked[boxes[i][k] = 'unlocked'

    opened = unlocked.values()

    if len(opened) != len(boxes):
        return False
    return True
