import torch
from models.TS2Vec import TS2Vec

class Base(object):
    def __init__(self,args):
        self.args = args
        self.model_dict = {
            'TS2Vec':TS2Vec,
            # 'TimeLLM':TimeLLM,
            # 'TimeMixer':TimeMixer
        }
        self.device = self._get_device()
        self.model = self._build_model().to(self.device)

    def _get_device(self):
        device = self.args.device if self.args.gpu else 'cpu'
        return device

    def _build_model(self):
        pass
    
    def train(self):
        pass
    
    def valid(self):
        pass
    
    def test(self):
        pass