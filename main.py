from collections import deque
from heapq import heappush, heappop 
import heapq

def shortest_shortest_path(graph, source):
# This will store the shortest path weight and number of edges for each vertex
  shortest_paths = {vertex: (float('inf'), float('inf')) for vertex   in graph}
  shortest_paths[source] = (0, 0)

# Priority queue to store vertices based on path weight and edge count
  priority_queue = [(0, 0, source)]  # (weight, edges, vertex)

  while priority_queue:
    current_weight, current_edges, current_vertex = heapq.heappop(priority_queue)

    for neighbor, weight in graph[current_vertex]:
        weight_via_current = current_weight + weight
        edges_via_current = current_edges + 1

        if (weight_via_current < shortest_paths[neighbor][0] or
            (weight_via_current == shortest_paths[neighbor][0] and edges_via_current < shortest_paths[neighbor][1])):
            shortest_paths[neighbor] = (weight_via_current, edges_via_current)
            heapq.heappush(priority_queue, (weight_via_current, edges_via_current, neighbor))

  return shortest_paths
    

    
    
def bfs_path(graph, source):
  parents = {source: None}
  queue = deque([source])

  while queue:
    current = queue.popleft()

    for neighbor in graph[current]:  # Treat neighbors as direct vertices
        if neighbor not in parents:
            parents[neighbor] = current
            queue.append(neighbor)

  return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    path = []
    step = destination

    # Traverse from the destination's parent back to the source
    if destination in parents:
        step = parents[destination]  # Start with the parent of the destination

    while step is not None and parents[step] is not None:
        path.append(step)
        step = parents[step]

    path.reverse()
    return path 

