from __feature__ import snake_case, true_property # type: ignore[import-not-found]

class Game:
    DIRECTION = ("w","a","s","d")

    def __init__(self):
        self.maze = (
            '┌S┬────────────────┬───────────┐',
            '│ │                │           G',
            '│ │ ┌─────┐ ┌───┬──┘ ┌───┬───┬─┤',
            '│ └─┘     │ │   │    │   │   │ │',
            '│     ┌─┐ │ │ │ │ ┌──┘ │ │ │ │ │',
            '│ ┌── │ │ │ │ │ │ │    │   │   │',
            '│ │   │   │ │ │ │ │ ┌──┴─┬─┴─┐ │',
            '│ │ ──┴───┘ │ │ │ │ │    │   │ │',
            '│ │         │ │   │ │  │ │ │ │ │',
            '│ └─────────┘ └───┴─┘  │ │ │ │ │',
            '│                      │   │   │',
            '└──────────────────────┴───┴───┘',
        )
        self.step =  0
        self.wall_hit = 0
        self.visited_cell = 0.0
        self.case_vide = None
        self.goal = False
        self.valid_move = False
        self.pos = (0,1)