def canFinish(numCourses, prerequisites):
    """
    Given a number of courses and the prerequisites, the 
    algorithm checks if it is possible to finish all the 
    courses.

    Time: O(N)
    Space: O(N)
    """
    #detect cycle of a directed graph
    def isCycle(graph, visited, i):
        #if in prgress node is a neighbour, it is a cycle
        if(visited[i] == 1):
            return True
        #if node has been processed, no cycle was found
        if(visited[i] == 2):
            return False
        #set node as currently being processed
        visited[i] = 1
        #check cycle on the neighbours of the current node
        for j in graph[i]:
            if(isCycle(graph, visited, j)):
                return False
        #node has been processed (all neigbours are visited)
        visited[i] = 2
        #no cycle found, return false
        return False
    
    #make graph
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]
    for i in prerequisites:
        graph[i[0]].append(i[1])
    
    #perform dfs on the nodes
    for i in range(len(graph)):
        if(isCycle(graph, visited, i)):
            return False
    return True

prereq = [[1,0], [0,1]]
assert False == canFinish(2, prereq)