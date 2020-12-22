def rottenOranges(grid):
    """
    Given a grid of oranges, a rotten orange is marked as 2,
    a fresh orange is marked as 1, and empty cells marked as 2.
    Every minute, a rotten orange will infect its adjacent neighbours.
    The algorithm will find the number of minutes till all fresh oranges
    become rotten (infected).

    Time: O(n*m)
    Space: O(n*m)
    """
    #list will be treated as queue for bfs
    rotten = []
    fresh = 0
    minutes = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 2):
                rotten.append([i,j])
            elif(grid[i][j] == 1):
                fresh+=1
                
    adjacent = [[0,1], [1,0], [-1,0], [0,-1]]
    #perform BFS
    while(rotten and fresh > 0):
        #completing each level of bfs
        for _ in range(len(rotten)):
            rotten_coord = rotten.pop(0)
            for i in adjacent:
                x = rotten_coord[0]+i[0]
                y = rotten_coord[1]+i[1]
                if(x >= 0 and x < len(grid) and y >= 0 
                    and y < len(grid[0]) and grid[x][y] == 1):
                    grid[x][y] = 2
                    fresh-=1
                    rotten.append([x,y])
        minutes+=1
    if(fresh == 0):
        return minutes
    return -1

A = [[2,1,1],[1,1,0],[0,1,1]]
assert 4 == rottenOranges(A)