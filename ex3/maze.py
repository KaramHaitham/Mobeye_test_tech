import queue

# Size of the maze
M = N = 10
# Use dedicated class for tuple and store parent tuple
class Node:
    def __init__(self, x, y, dist, parent):
        self.x = x
        self.y = y
        self.dist = dist
        self.parent = parent

# Check if it is possible to visit adjacent node/not out of bound 
# and is a path/not a wall
# and has not been visited yet
def isValid(matrix, visited, x, y):
    return x >= 0 and x < M and y >= 0 and y < N and matrix[x][y] == 1 and visited[x][y] == 0

def printPath(node):
    if(node == 0):
        return
    printPath(node.parent)
    print('({0}, {1})'.format(node.x, node.y))

def BroadFirstSearch(matrix, i, j, x, y): #i,j startPoint and x,y endPoint

    # construct a matrix of unvisited node
    visited = [[0 for x in range(N)] for y in range(M)]
    
    # set the current node as visited
    visited[i][j] = 1
    
    # construct an empty queue to keep track of which nodes are kept as shortest path element
    nodeQueue = queue.Queue() # fifo queue 
    nodeQueue.put(Node(i, j, 0, 0))
    # variable to store the minimum cost
    minDist = 999999 # use a great value as it is the begining
    currentNode = 0
    while not nodeQueue.empty():
        currentNode = nodeQueue.get(0)
        
        i = currentNode.x
        j = currentNode.y
        dist = currentNode.dist
        
        # if we reach the end stop the search
        if(i == x and j == y):
            minDist = dist
            break
        
        # explore all adjacent nodes
        row = [-1, 0, 0, 1] # [up, 0, 0, down]
        col = [0, -1, 1, 0] # [0, left, right, 0]
        for availableRoute in range(0, 4):
            if(isValid(matrix, visited, i + row[availableRoute], j + col[availableRoute])):
                visited[i + row[availableRoute]][j + col[availableRoute]]=1
                # Add available roots to queue to explore
                nodeQueue.put(Node(i + row[availableRoute], j + col[availableRoute], dist + 1, currentNode))
    
    if(minDist != 999999):
        print('The shortest distance is {0}'.format(minDist))
        printPath(currentNode)
    else:
        print('The end node cannot be reached from the starting node')


mat = [
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

BroadFirstSearch(mat, 0, 0, 7, 5)
    
    