#!/usr/bin/python3
"""A method that determines if all the boxes can be opened in a locked boxes"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        for key in boxes[current_box]:
            if not visited[key]:
                stack.append(key)

    # If all boxes are visited, then return True, else return False
    return all(visited)
