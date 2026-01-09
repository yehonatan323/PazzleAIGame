from search_node import search_node
from color_blocks_state import color_blocks_state
import heapq

def create_open_set():
    return ([], {})     # heap, hash: blocks → g

def create_closed_set():
    return {}           # hash: blocks → g

def add_to_open(node, open_set):
    heap, mapping = open_set
    heapq.heappush(heap, (node.g + node.h, node.g, node.state.blocks, node.prev))
    mapping[node.state.blocks] = node.g

def open_not_empty(open_set):
    return len(open_set[1]) > 0

def get_best(open_set):
    heap, mapping = open_set
    while heap:
        f, g, blocks, prev = heapq.heappop(heap)
        if blocks in mapping and mapping[blocks] == g:
            state = color_blocks_state(blocks)
            return search_node(state, g, f-g, prev)
    return None

def add_to_closed(node, closed):
    closed[node.state.blocks] = node.g

def duplicate_in_open(node, open_set):
    mapping = open_set[1]
    b = node.state.blocks
    if b in mapping:
        if node.g >= mapping[b]:
            return True
        mapping[b] = node.g
    return False

def duplicate_in_closed(node, closed):
    b = node.state.blocks
    if b in closed:
        if node.g >= closed[b]:
            return True
        closed.pop(b)
    return False

def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node)
        if node.prev is None:
            break
        node = search_node(color_blocks_state(node.prev), node.g-1, 0, None)
    return path[::-1]

def search(start_state, heuristic):
    open_set = create_open_set()
    closed = create_closed_set()

    start = search_node(start_state, 0, heuristic(start_state), None)
    add_to_open(start, open_set)

    while open_not_empty(open_set):
        current = get_best(open_set)

        if color_blocks_state.is_goal_state(current.state):
            return reconstruct_path(current)

        add_to_closed(current, closed)

        for ns, cost in current.state.get_neighbors():
            g = current.g + cost
            node = search_node(ns, g, 0, current.state.blocks)

            if duplicate_in_closed(node, closed):
                continue
            if duplicate_in_open(node, open_set):
                continue

            node.h = heuristic(ns)
            add_to_open(node, open_set)

    return None
