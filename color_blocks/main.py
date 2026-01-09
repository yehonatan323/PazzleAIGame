import time
from heuristics import *
from color_blocks_state import *
from search import *

if __name__ == '__main__':

    start_blocks = "(70,7),(80,8),(9,90),(10,100),(11,111),(12,122),(1,10),(2,20),(3,30),(4,40),(5,50),(6,60)"
    goal_blocks = "1,2,3,7,8,12,4,5,6,9,10,11"
    
    s = color_blocks_state("(5,2),(1,3),(9,22),(21,4)")

    init_goal_for_heuristics(goal_blocks)
    init_goal_for_search(goal_blocks)
    start_state = color_blocks_state(start_blocks)
    start_time = time.time()
    search_result = search(start_state, advanced_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)
