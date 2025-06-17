from pipe.base import Base

class Inference(Base):
    def __init__(self,args):
        super(Inference,self).__init__(args)

    def _build_model(self):
        pass
    
    def inference(self):
        pass