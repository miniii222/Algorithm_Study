graph1 = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'F']),
         'C': set(['A', 'G']),
         'D': set(['B']),
         'E': set(['A', 'F']),
         'F': set(['B', 'E']),
         'G': set(['C'])}

graph2 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

korea = {'세종': set(['서울', '강릉', '대구', '광주']),
         '서울': set(['평양', '인천', '세종']),
         '강릉': set(['독도', '세종']),
         '광주': set(['세종', '여수']),
         '대구': set(['세종', '울산']),
         '평양': set(['서울', ]),
         '인천': set(['서울', ]),
         '독도': set(['강릉', ]),
         '여수': set(['광주', '부산']),
         '울산': set(['대구', '부산']),
         '부산': set(['여수', '울산']),
         }
#%%
network = {
        'A' : set(['C',"D",'E','F']),
        	'C' : set(['A','D','G','H']),
        	'D' : set(['A',"C",'E','H']),
        	'E' : set(['A','D','F','I']),
        	'F' : set(['A','E','I','J']),
        	'G' : set(['C','H','B']),
        	'H' : set(['C','D','G','I','B']),
        	'I' : set(['E','F','H','J','B']),
        	'J' : set(['F','I','B']),
        	'B' : set(['G','H','I','J'])
        }
#%%
def DFS(graph, start) :
    stk = []
    stk.append(start)
    visited = []
        
    while len(stk) :
        visiting = stk.pop()
        
        if visiting not in visited :
            stk.extend(graph[visiting]-set(visited))
            visited.append(visiting)
            
    return visited

DFS(network, 'A')

#%%
def DFS_path(graph, start, goal,visited=[]) :
    path = []
    visited = visited + [start]
    
    if start == goal :
        path.append(visited)
        print(path)
    
    for child  in graph[start] :
        if child not in visited :
            DFS_path(graph,child,goal,visited)

DFS_path(graph1, 'C',"D")
DFS_path(korea, '부산','평양')     
#%%
def BFS(graph, start) :
    queue = [start]
    visited = []
    
    while len(queue) :
        visiting = queue.pop(0)
        if visiting not in visited :
            queue.extend(graph[visiting]-set(visited))
            visited.append(visiting)
            
    return(visited)

BFS(network,'A')           
    
    
#%%
def BFS_path(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result

BFS_path(network,'A', 'B')

#%%
paths=[]
def BFS_path(graph, start, end, path=[]):
    
    path = path + [start]
    if start == end:
        paths.append(path)
    
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        for node in graph[vertex]:
            if node not in path:
                BFS_path(graph, node, end, path)



BFS_path(network,'A', 'B')
len(paths)
