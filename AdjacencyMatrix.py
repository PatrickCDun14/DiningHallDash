import pandas as pd

class AdjacencyMatrix:
    def __init__(self,file_name):
        self.matrix=pd.read_excel(file_name).iloc