def maxAreaOfIsland(grid):
    """
    Given a grid consisting of 1's and 0's, the 
    algorithm finds the size of the largest sequence
    of 1s in the grid. A sequence is defined as if any
    of the adjacent neighbours are also 1.

    Time: O(n*m) 
    Space: O(1)
    """
    def dfs(grid, i, j):
        #mark as visited
        grid[i][j] = 2
        #keep track of the number of nodes
        k = 0
        #perform DFS and add to the number of nodes (+1 for current node)
        if(i+1 < len(grid) and grid[i+1][j] == 1):
            k+=1+dfs(grid,i+1,j)
        if(i-1 >= 0 and grid[i-1][j] == 1):
            k+=1+dfs(grid,i-1,j)
        if(j+1 < len(grid[0]) and grid[i][j+1] == 1):
            k+=1+dfs(grid,i,j+1)
        if(j-1 >= 0 and grid[i][j-1] == 1):
            k+=1+dfs(grid,i,j-1)  
        return k
    
    size = 0
    #go through all the elements in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 1):
                #keep track of the maximum size
                size = max(size, dfs(grid,i,j)+1)
    return size