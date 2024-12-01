import json
from .util import PointDict

class Board(object):
    def __init__(self, next_color='BLACK'):
        self.winner = None
        self.next = next_color  # Initializes `next` here
        self.legal_actions = []  # Legal actions for current state
        self.end_by_no_legal_actions = False
        self.counter_move = 0

        # Point dict
        self.libertydict = PointDict()  # {color: {point: {groups}}}
        self.stonedict = PointDict()

        # Group list
        self.groups = {'BLACK': [], 'WHITE': []}
        self.endangered_groups = []  # groups with only 1 liberty
        self.removed_groups = []  # This is assigned when game ends
