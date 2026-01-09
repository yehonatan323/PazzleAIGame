GOAL_VISIBLE = [] 

def init_goal_for_search(goal_blocks):
    global GOAL_VISIBLE
    GOAL_VISIBLE = [int(x) for x in goal_blocks.split(",")]

class color_blocks_state:
    __slots__ = ("blocks",)   # ↓ חיסכון עצום בזיכרון

    def __init__(self, blocks):
        if isinstance(blocks, str):
            s = blocks.replace(" ", "").replace("),(", ")|(")
            lst = []
            for p in s.split("|"):
                p = p.replace("(", "").replace(")", "")
                a, b = p.split(",")
                a, b = int(a), int(b)
                # normalize pairs
                lst.append((a, b))
            self.blocks = tuple(lst)
        else:
            self.blocks = tuple(blocks)

    def __hash__(self):
        return hash(self.blocks)

    def __eq__(self, other):
        return isinstance(other, color_blocks_state) and self.blocks == other.blocks

    @staticmethod
    def is_goal_state(state):
        visible = [v for (v,h) in state.blocks]
        return visible == GOAL_VISIBLE

    def get_neighbors(self):
        neighbors = []
        blocks = self.blocks
        n = len(blocks)

        # SPIN
        for i in range(n):
            lst = list(blocks)
            v, h = lst[i]
            lst[i] = (h, v)
            neighbors.append((color_blocks_state(tuple(lst)), 1))

        # FLIP
        for k in range(2, n+1):
            prefix = blocks[:-k]
            suffix = blocks[-k:]
            neighbors.append((color_blocks_state(prefix + tuple(reversed(suffix))), 1))

        return neighbors

    def get_state_str(self):
        return ",".join(f"({v},{h})" for (v,h) in self.blocks)
