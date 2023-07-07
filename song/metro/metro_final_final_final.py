import pandas as pd

graph = pd.read_csv("./subway.csv").values.tolist()
location = pd.read_csv("./subwayLocation.csv").values.tolist()

def nodes(gr):
    node = set()
    for edge in gr:
        node.add(edge[0])
        node.add(edge[1])
    return sorted(node)

class MainClass:

    def __init__(self):
        self.node = nodes(graph)
        self.station_list = list()
        self.route_result_name = list()
        self.route_result_location = list()
        self.input_data1 = None
        self.input_data2 = None

        for i in self.node:
            self.station_list.append(i)

    def setInformation(self, location1, location2):
        self.input_data1 = location1
        self.input_data2 = location2

    def findLocation(self, node, location):
        point = []
        for n in node:
            for l in location:
                if n[-4::-1] == l[0][-1::-1]:
                    point.append([float(l[1]), float(l[2])])
                    break
        return point

    def programRun(self):
        global location

        dj = Dijkstra(self.node)

        start = self.input_data1
        end = self.input_data2

        path = self.findLocation(dj.getPath(start, end), location)
        self.route_result_name = dj.getPath(start, end)
        self.route_result_location = path

    def getInformation(self):
        return self.route_result_name, self.route_result_location

    def getTotalLocation(self):
        return location

    def getTotalName(self):
        temp_list = list()
        for data in graph:
            temp_list.append(data[0])
        return temp_list

    def getGraph(self):
        return graph

class Dijkstra:
    def __init__(self, node):
        self.g = {}
        self.dist = {}
        for n in node:
            self.g[n] = {}
            self.dist[n] = [float('inf'), "none"]

        global graph
        for i in graph:
            self.setEdge(i[0], i[1], int(i[2]))
    
    def setEdge(self, start, end, distance):
        self.g[start][end] = distance
        self.g[end][start] = distance
    
    def getPath(self, start, end):
        
        visit = nodes(graph)

        dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])

        curNode = start
        
        # 현재 노드의 거리는 0으로
        self.dist[curNode][0] = 0

        while True:
            visit.remove(curNode)
            next_to = self.g[curNode]

            for i in next_to:
                if min(self.dist[i][0], self.dist[curNode][0] + self.g[curNode][i]) < self.dist[i][0]:
                    self.dist[i][0] = min(self.dist[i][0], self.dist[curNode][0] + self.g[curNode][i])
                    self.dist[i][1] = curNode

            if len(visit) > 0:
                curNode = min(dictfilt(self.dist, visit), key=dictfilt(self.dist, visit).get)
            else:
                break

        path = [end]
        dist = []

        while end != start:
            path.append(self.dist[end][1])
            dist.append(self.dist[end][0])
            end = self.dist[end][1]

        return path[::-1]

