from color_blocks_state import color_blocks_state

GOAL_ADJ = set()
GOAL_POS = {}

def init_goal_for_heuristics(goal_blocks):
    global GOAL_ADJ, GOAL_POS
    goal_list = [int(x) for x in goal_blocks.split(",")]
    GOAL_POS = {c: i for i, c in enumerate(goal_list)}

    GOAL_ADJ = {
        (goal_list[i], goal_list[i+1])
        for i in range(len(goal_list)-1)
    } | {
        (goal_list[i+1], goal_list[i])
        for i in range(len(goal_list)-1)
    }

def base_heuristic(state):
    blocks = state.blocks
    h = 0
    for i in range(len(blocks)-1):
        v1, h1 = blocks[i]
        v2, h2 = blocks[i+1]
        if (v1,v2) not in GOAL_ADJ and \
           (v1,h2) not in GOAL_ADJ and \
           (h1,v2) not in GOAL_ADJ and \
           (h1,h2) not in GOAL_ADJ:
            h += 1
    return h

def advanced_heuristic(state):
    h = base_heuristic(state)
    extra = 0
    for (v,h2) in state.blocks:
        if v not in GOAL_POS and h2 not in GOAL_POS:
            extra += 1
    return h + extra
