import pandas as pd

class XAUUSD:
    def __init__(self,args):
        self.args = args
        self.data = pd.read_csv('/home/schaffen/Workspace/Project/TS2Vec/data/XAUUSD_M5.csv')
        self.data = self.data.drop(columns=['Unnamed: 0'])
        self.data = self.data.dropna()
        self.data = self.data.reset_index(drop=True)
        self.data = self.data.drop(columns=['Unnamed: 0'])
        self.data = self.data.dropna()
        self.data = self.data.reset_index(drop=True)