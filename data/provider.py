import pandas as pd
from data.loader import XAUUSD
from torch.utils.data import DataLoader

class Provider:
    def __init__(self,args,flag='train'):
        self.args = args
        self.data_dict = {
            'XAUUSD': XAUUSD
        }
        self.data_set = self._init_dataset()
        self.data_loader = self._data_loader()

    def _init_dataset(self):
        return self.data_dict[self.args.data](
            flag=self.flag,
            root_path=self.args.root_path,
            data_path=self.args.data_path,
            target=self.args.target,
            time_var=self.args.time_var,
            input_len=self.args.input_len,
            output_len=self.args.output_len,
            batch_size=self.args.batch_size,
        )
    
    def _data_loader(self):
        return DataLoader(self.data_set,batch_size=self.args.batch_size,shuffle=True)
    
    
    def __getitem__(self):
        return self.data_set, self.data_loader