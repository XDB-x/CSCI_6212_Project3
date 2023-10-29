# This just pseudocode
function findDiameter(G):
    maxDiameter = 0
    for each vertex v in G:
        distance = BFS(G, v)
        maxDistance = max(distance)
        if maxDistance > maxDiameter:
            maxDiameter = maxDistance
    return maxDiameter

function BFS(G, startVertex):
    create a queue Q
    create a distance array distance[], initialize all values to -1
    enqueue startVertex to Q
    set distance[startVertex] = 0
    while Q is not empty:
        currentVertex = dequeue from Q
        for each neighbor n of currentVertex:
            if distance[n] == -1:
                enqueue n to Q
                set distance[n] = distance[currentVertex] + 1
    return distance
