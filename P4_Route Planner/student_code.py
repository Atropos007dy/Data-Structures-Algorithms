from math import sqrt
from queue import PriorityQueue


def shortest_path(M, start, goal):
    
    def get_distance(M, node1, node2):        
        x1, y1 = M.intersections[node1]
        x2, y2 = M.intersections[node2]
        distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return distance
    
    def path_finder(paths, start, goal):
        cur = goal
        path = [cur]
        while cur != start:
            cur = paths.get(cur, None)
            if not cur:
                return None
            path.append(cur)
        return path[::-1]
    
    print("shortest path called")
    
    
    #initialization 
    frontier = PriorityQueue()
    paths = {start: None}
    G = {start: 0} 
    H = {}
    
    
    for node, _ in M.intersections.items():
        H[node] = get_distance(M, node, goal)
        
    frontier.put(start, H[start])

    while not frontier.empty():
        cur_node = frontier.get()
        
        if cur_node == goal:
            path_finder(paths, start, goal)
        
        for neighbor in M.roads[cur_node]:
            g_temp = G[cur_node] + get_distance(M, cur_node, neighbor)
            if neighbor not in G or g_temp < G[neighbor]:
                G[neighbor] = g_temp
                f = g_temp + H[neighbor] 
                frontier.put(neighbor, f)
                paths[neighbor] = cur_node
                
    return path_finder(paths, start, goal) 