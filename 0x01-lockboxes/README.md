README for Lockboxes Coding Challenge

This coding challenge involves a list of lockboxes, each containing keys to other lockboxes. The goal is to determine if all the lockboxes can be opened by recursively checking if each key can open another lockbox until all lockboxes have been opened.

To solve this challenge, you can use a depth-first search algorithm to traverse the lockboxes and their keys. You can keep track of which lockboxes have been opened using a set, and use a stack to keep track of the keys that have been found but not yet used to open another lockbox.

The main function for this challenge is canUnlockAll(boxes), which takes in a list of lockboxes and returns True if all the lockboxes can be opened, and False otherwise.

Example usage:
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True

For more information on the Lockboxes Coding Challenge, visit the ALX website.
