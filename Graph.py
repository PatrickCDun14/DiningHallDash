import pandas as pd
import sys


class Graph:
    
    def __init__(self,file_name):    
        self.adjacencyMatrix=pd.read_excel(file_name,index_col=0)
    
    def getNeighbors(self,dining_hall):
        neighbors=self.adjacencyMatrix[dining_hall]
        table=dict()
        for i in range(len(neighbors)):
            if neighbors[i]!=0:
                table[self.adjacencyMatrix.index[i]] = neighbors[i]
        return table
    
    def getNearestNeighbors(self, dining_hall):
        table = self.getNeighbors(dining_hall)
        min=1000
        neighborIndexes=[]
        for i in range(len(list(table.items()))):
            if list(table.items())[i][1]==min:
                neighborIndexes.append(i)
            elif list(table.items())[i][1] < min:
                neighborIndexes.clear()
                neighborIndexes.append(i)
                min=list(table.items())[i][1]
        neighbors = dict()
        for x in neighborIndexes:
            neighbors[list(table.keys())[x]] = list(table.items())[x][1] 
        return neighbors
    
    def printPath(self, path):
        p = ""
        for i in range(len(path)):
            if i==0:
                p+=path[i]
            else:
                p+=" -> " + path[i]
        print(p)
                
    #Naive solution
    def BruteForce(self):
        #{path sum,path} 
        result = []
        #create a copy of the dataframe's row labels
        dining_halls=list((self.adjacencyMatrix.index).copy())
        self.permute(result,dining_halls,0,len(dining_halls)-1)
        minSum = sys.maxsize
        minPath = []
        for path in result:
            pathSum=self.pathSum(path)
            if pathSum < minSum:
                minSum=pathSum
                minPath=path
        self.printPath(minPath)
        print(minSum)

    #recursively computes all possible traversal orders    
    def permute(self,result, array, startIndex, endIndex):
    #base case
        if startIndex==endIndex:
            result.append(array.copy())
        else:
            for i in range(startIndex,endIndex):
                #swap start index and i
                array[startIndex], array[i]= array[i], array[startIndex]
                self.permute(result,array,startIndex+1,endIndex)
                #swap them back
                array[startIndex], array[i] = array[i], array[startIndex]
    
    #utility function to find the edge between two vertices
    def edgeLookUp(self,hall1,hall2):
        halls = list(self.adjacencyMatrix.index)
        return self.adjacencyMatrix[hall1][halls.index(hall2)]

    #utility functinon to find the total cost of a path
    def pathSum(self,path):
        sum=0
        for i in range(1,len(path)):
            sum+=self.edgeLookUp(path[i-1],path[i])
        return sum 
    
    def sortedEdges(self):
        edges = {}
        for vertex in self.adjacencyMatrix.index:
            for i in range(len(self.adjacencyMatrix.index)):
                weight=self.adjacencyMatrix[vertex][i]
                if weight!=0:
                    edgeName = vertex + ">" + self.adjacencyMatrix.index[i]
                    edges.update({edgeName:weight})
        return dict(sorted(edges.items(),key=lambda e : e[1]))

    #utility function finds the nearest neighbor that hasn't been visited
    def minVertex(self,vertex,visited):
        minVertex = sys.maxsize
        for v in range(len(self.adjacencyMatrix.index)):
            if vertex[v] < minVertex and not visited[v]:
                minVertex = vertex[v]
                index = v
        return index
    
    #used to construct an MST for the graph       
    def PrimMST(self):
        #stores vertices that are the lowest distance from eachother
        verticies = [sys.maxsize] * len(self.adjacencyMatrix.index)
        #stores mst
        mst = [None] * len(self.adjacencyMatrix.index)
        verticies[0]=0
        #keeps track of which vertices have been visited
        visited = [False] * len(self.adjacencyMatrix.index) 
        mst[0]=-1
        for i in range(len(self.adjacencyMatrix.index)):
            minVertex = self.minVertex(verticies,visited)
            visited[minVertex]=True
            for v in range(len(self.adjacencyMatrix.index)):
                
                if self.adjacencyMatrix.iloc[minVertex][v]>0 and not visited[v] and verticies[v]:
                    verticies[v]=self.adjacencyMatrix.iloc[minVertex][v]
                    mst[v]=minVertex
        #construct an adjacency list representation of the resulting MST
        adjacencyList = []
        for i in range(len(self.adjacencyMatrix.index)):
            adjacencyList.append([])
        for i in range(1, len(self.adjacencyMatrix.index)):
            adjacencyList[mst[i]].append(i) 
            adjacencyList[i].append(mst[i])
        return adjacencyList
    
    def dfs(self,mst,source,path,visited):
        #add vertex to path 
        path.append(self.adjacencyMatrix.index[source])
        visited[source]=True
        for v in mst[source]:
            if visited[v]==False:
                self.dfs(mst,v,path,visited)
        
    def approximateShortestPath(self):
        #generate minimum spanning tree
        mst = self.PrimMST()
        visited=[False]*len(self.adjacencyMatrix.index)
        path=[]
        #preorder traversal
        self.dfs(mst,0,path,visited)
        self.printPath(path)
        print(self.pathSum(path))







