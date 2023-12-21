ListOfAirports = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"
]


ListOfRoutes = [
    ["DSM", "ORD"], ["ORD", "BGI"], ["BGI", "LGA"], ["SIN", "CDG"], ["CDG", "SIN"], ["CDG", "BUD"],
    ["DEL", "DOH"], ["DEL", "CDG"], ["TLV", "DEL"], ["EWR", "HND"], ["HND", "ICN"], ["HND", "JFK"],
    ["ICN", "JFK"], ["JFK", "LGA"], ["EYW", "LHR"], ["LHR", "SFO"], ["SFO", "SAN"], ["SFO", "DSM"],
    ["SAN", "EYW"]
]
StartPoint = 'LGA'

lengthBeforeAddingAnyRoutes = len(ListOfRoutes)

adj = [[0] * len(ListOfAirports) for _ in range(len(ListOfAirports))]
depth = [0] * len(ListOfAirports)
allVisited = []


def prepareAdjacencyMatrix(airports, routesList):
    for route in routesList:
        i = airports.index(route[0])
        j = airports.index(route[1])
        adj[i][j] = 1


def getDepthForIndividual(airportIndex, visitedArrayParam):
    visitedArrayParam.append(airportIndex)
    Sum = 0
    for j in range(len(adj[airportIndex])):
        if adj[airportIndex][j] == 1 and j not in visitedArrayParam:
            Sum += 1 + getDepthForIndividual(j, visitedArrayParam)
    return Sum


def repeatProcess():
    prepareAdjacencyMatrix(ListOfAirports, ListOfRoutes)
    for i in range(len(adj)):
        visitedArray = []
        depth[i] = getDepthForIndividual(i, visitedArray)
        allVisited.append(visitedArray)


counter = 0

while depth[ListOfAirports.index(StartPoint)] != len(ListOfAirports) - 1:
    allVisited = []
    repeatProcess()
    flag = 0
    while flag == 0:
        indexOfMaxDepth = depth.index(max(depth))
        if ListOfAirports.index(StartPoint) != indexOfMaxDepth and indexOfMaxDepth not in allVisited[ListOfAirports.index(StartPoint)]:
            ListOfRoutes.append([StartPoint, ListOfAirports[indexOfMaxDepth]])
            flag = 1
            counter += 1
        elif depth[ListOfAirports.index(StartPoint)] == len(ListOfAirports) - 1:
            break
        else:
            depth[indexOfMaxDepth] = 0

print(counter)
