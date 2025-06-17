import torch
import torch.nn as nn

class TS2Vec(nn.Module):
    def __init__(self,args):
        super(TS2Vec,self).__init__()
        self.args = args

    def forward(self,x):
        pass