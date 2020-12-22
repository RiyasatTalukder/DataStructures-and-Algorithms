def numberOfIslands(grid: List[List[str]]): 
    """
    Given a grid of strings with values '1' and '0', The algorithm
    finds the number of islands that is present in the grid. An island
    is defined to be of adjacent values of '1'.

    Time: O(n*m)
    Space: O(n*m)

    """
    n = len(grid)
    m = len(grid[0])
    def DFS(grid, visited, i, j):
        visited[i][j] = 1
        if(i-1 >= 0 and not visited[i-1][j] and grid[i-1][j] == '1'):
            DFS(grid, visited, i-1, j)
        if(i+1 < n and not visited[i+1][j] and grid[i+1][j] == '1'):
            DFS(grid, visited, i+1, j)
        if(j-1 >= 0 and not visited[i][j-1] and grid[i][j-1] == '1'):
            DFS(grid, visited, i, j-1)
        if(j+1 < m and not visited[i][j+1] and grid[i][j+1] == '1'):
            DFS(grid, visited, i, j+1)
    
    islands = 0
    visited = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == '1' and not visited[i][j]):
                DFS(grid, visited, i, j)
                islands+=1
    
    return islands