import heapq
from collections import deque

"""
    returns array of of shortest distance from start node to all other nodes 
"""
def dijkstras_1(adj_list: list[list[tuple[int,int]]], start:int)-> list[int]:
    
    
    
    """
    init priority queue
    set array for -1 for unvisited nodes
    while there are nodes in the queue
        get node with current shortest distance
        if node already has a confirmed shortest distance
        mark the shortest distance for this node 
    """
    
    
    
    q = [(0,start)]
    dist = [-1] * len(adj_list)
    
    while q:
        curr_dist,curr = heapq.heappop(q)
        if dist[curr] != -1:
            continue
        dist[curr] = curr_dist
        
        for nbr, weight in adj_list[curr]:
            if dist[nbr] == -1:
                heapq.heappush(q, (curr_dist + weight, nbr))
    return dist

def dijkstras_2(adj_list: list[list[tuple[int, int]]], start: int) -> list[int]:
    
    q = [(0, start)]
    dist = [float("inf")] * len(adj_list)
    dist[start] = 0
    
    while q:
        curr_dist, curr = heapq.heappop(q)
        if curr_dist > dist[curr]:
            continue

        for nbr, weight in adj_list[curr]:
            new_dist = curr_dist + weight
            if new_dist < dist[nbr]:
                dist[nbr] = new_dist
                heapq.heappush(q, (new_dist, nbr))
    return dist

def bfs_with_paths(adj_list: list[list[int]], start: int) -> tuple[list[int], list[list[int]]]:
    """
    run bfs to find distances and shortesst paths  
adj_list: weighted graph
start: start vertex
returns:
    distance array 
    
    graph = []
    dist,paths = bfs_with_paths(graph,0)
    dist

    paths 
    
    
    
    init queue 
    
    pop next node in the queue 
    if neighbor has not been visited
    add neighbor to the queue for future processing
    update shortest distance for the neighbor
    set parent for path reconstruction
    
    make paths from current array 
    
    """
    q = deque([start])
    dist = [-1] * len(adj_list)
    dist[start] = 0
    parent = [-1] * len(adj_list)
    
    while q:
        curr = q.pop()
        for nbr in adj_list[curr]: # loop for neighbhors 
            if dist[nbr] == -1: # do if nbr not visited
                q.appendleft(nbr) # add neighbhor to queue for future processing
                dist[nbr] = dist[curr]+ 1 # update shortest ditance from neighbhor
                parent[nbr] = curr # set parent to remake the path
    paths = [] # init list to store paths for each node 
    
    for node in range(len(adj_list)):
        path = node[node] # star path with current node 
        curr = node 
        while parent[curr] != -1: # traverse back using parent array
            curr = parent[curr] #move to parent node
            path.append(curr) #append node to path
        path.reverse() # reverse path to get order from start to node 
        paths.append(path) # add new path to paths list

    return dist,paths # return dist and paths 
        
    
