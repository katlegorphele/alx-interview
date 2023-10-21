#!/usr/bin/python3

'''
Method that determines if all boxes can be opened
'''

def canUnlockAll(boxes):
    # Create a list to keep track of the boxes that have been opened
    opened_boxes = [0]
    
    # Create a list to keep track of the keys that are available
    available_keys = boxes[0]
    
    # Loop through the available keys until there are no more keys left
    while available_keys:
        # Pop the first key from the list of available keys
        key = available_keys.pop(0)
        
        # Check if the key opens a new box
        if key < len(boxes) and key not in opened_boxes:
            # Add the new box to the list of opened boxes
            opened_boxes.append(key)
            
            # Add the keys from the new box to the list of available keys
            available_keys.extend(boxes[key])
    
    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

