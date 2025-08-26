from collections import deque

def bfs(root_node, goal_value):
    path_queue = deque()
    initial_path = [root_node]
    path_queue.appendleft(initial_path)
  
# Implement search loop below
while len(path_queue) > 0:
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f'Output string {current_node.value}')
    if current_node.value == goal_value:
        return current_path
    return None