import torch
from pipe.base import Base

class Trainer(Base):
    def __init__(self,args):
        super(Trainer,self).__init__(args)

    def _build_model(self):
        model = self.model_dict[self.args.model](self.args)
        return model
    
    def train(self):
        pass
    
    def valid(self):
        pass
    
    def test(self):
        pass