from helpers import get_path, offset, is_legal_path
from priority_queue import Priority_queue

def heuristic(a, b):
    """
    Calculate the Manhattan distance between two pairs of grid coordinates
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x2-x1) + abs(y2 -y1)