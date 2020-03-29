def min_dst(dst, queue):
    """
    objective: function to find the vertex with minimum dist value, from the set of vertices still in queue
    @param : dist(containg inf for unvisited vertices) and queue(conatining all vertices)
    @returnValue : min_index(vertex with minimum distance value)
    """
    minimum = float('inf')  #initializing minimum variable with highest value
    min_index = -1  #initializing min_index with minimum value

    for dst_iterator in range(len(dst)):  #iterating through dst list
        if dst[dst_iterator] < minimum and dst_iterator in queue:
            #checking if dst list has minimum distance
            minimum = dst[dst_iterator]
            min_index = dst_iterator
    return min_index


def appendpaths(paths, startingpoint, endingpoint, cost, srcEnum, dstEnum):
    """
    objective: function to append paths all the way from source to destination 
    @param : paths, startingpoint, endingpoint, cost, srcEnum, dstEnum
        paths --> list of lists containing enumerated value corresponding to places together with costs
        startingpoint --> starting point of new path
        endingpoint --> ending point of new path
        cost --> cost to replace after appending path
        srcEnum --> enumerated value of ultimate source
        dstEnum --> enumerated value of ultimate destination
    @returnValue : paths(list of path after appending new path and replacing cost)
    """
    print(paths)
    for path in paths:
        if (path[len(path) - 2] == startingpoint
                and path[len(path) - 2] != dstEnum):
            path.insert(len(path) - 1, dstEnum)
            path[len(path) - 1] = cost
    return (paths)


def minimumCostRoute(noOfVertices, adjMat, srcEnum, dstEnum):
    """
    objective: function to return list of paths together with cost
    @param : noOfVertices, adjMat, srcEnum, dstEnum
        noOfVertices --> number of vertices
        adjMat --> adjancey matrix denoting graph
        srcEnum --> enumerated value of ultimate source
        dstEnum --> enumerated value of ultimate destination 
        
    @returnValue : paths(list of all possible paths together with cost)
    """
    dst = [float("inf")] * noOfVertices

    queue = []
    for i in range(noOfVertices):
        queue.append(i)

    dst[srcEnum] = 0
    paths = []
    while queue:
        u = min_dst(
            dst, queue
        )  # vertex with minimum distance from the vertices still in queue
        queue.remove(u)  # removing minimum value index in distace list

        for x in range(noOfVertices):
            '''Update dist[x] only if it is in queue, there is 
                an edge from u to x, and total weight of path from 
                src to x through u, which is smaller than the  current value of 
                dist[x]'''
            if adjMat[u][x] and x in queue:
                if adjMat[u][x] + dst[u] < dst[x]:
                    dst[x] = adjMat[u][x] + dst[u]
                    if u == srcEnum:
                        """edge from u to x, if edge equals to ultimate source 
                        the path of edge from u to x is added in paths list
                        """
                        paths.append([u, x, dst[x]])
                    else:
                        """edge from u to x, if edge not equals to ultimate source 
                        the path of edge from u to x is must be appended with respective 
                        path where ending edge is equal to u
                        """
                        paths = appendpaths(paths, u, x, dst[x], srcEnum,
                                            dstEnum)

    return (paths)


# input for final source nd destination
final_src, final_dst = input().split(" ")

srcs = []
dsts = []
costs = []
while (True):
    inputs = input()
    if (inputs != "0"):
        # next line inputs with source and departure city name with costs
        u, v, cost = inputs.split(" ")
        srcs.append(u)
        dsts.append(v)
        costs.append([u, v, cost])
    else:
        # iteration breaks if user enters 0
        break

#total number of vertices
vertices = list(set(srcs + dsts))
#creating dicionary with enumerated value against vertices
verticesEnum = dict(zip(vertices, range(len(vertices))))

# preparing adjacency matrix
adjMat = []
for u in range(len(srcs)):
    #initializing matrix with inf value
    rows = []
    for v in range(len(dsts)):
        if (u == v):
            rows.append(0)
        else:
            rows.append(float('inf'))
    adjMat.append(rows)

for x in costs:
    # replacing inf vaue with weights(costs) as per the source and departure stations provided
    adjMat[verticesEnum[x[0]]][verticesEnum[x[1]]] = int(x[2])

# list of paths with costs
all_paths = minimumCostRoute(
    len(srcs), adjMat, verticesEnum[final_src], verticesEnum[final_dst])

keysSet = list(verticesEnum.keys())  # keys Set of dictionary
for path in all_paths:
    #iterating all paths and printing them with source,
    #immediate stations, destination with costs
    for route_iterator in range(len(path) - 1):
        print(keysSet[path[route_iterator]], end=" ")
    print(path[route_iterator + 1], end="\n")
