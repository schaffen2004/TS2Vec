import argparse
import random
import torch #
import numpy as np

def set_seed(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    np.random.seed(seed)

def get_config():
    parser = argparse.ArgumentParser(description='TS2Vec')
    
    # basic config
    parser.add_argument("--training",type=bool,required=True,default=True)
    parser.add_argument("--model",type=str,required=True,default="TS2Vec",
                        help="model name, options: TS2Vec, TimeLLM, TimeMixer")
    parser.add_argument("--seed",type=int,default=2021,help="random seed")

    # data loader
    parser.add_argument("--root_path",type=str,required=True,default="./data/")
    parser.add_argument("--checkpoints",type=str,required=True,default="./checkpoints/")
    parser.add_argument("--data_path",type=str,required=True,default='XAUUSD_M5.csv')
    parser.add_argument("--target",type=str,required=True,default="CandleType",help="target variable")
    parser.add_argument("--time_feature",type=str,required=True,default="Time",help="time feature variable, options: Time, Date")

    # model define

    # optimization


    # GPU
    parser.add_argument("--gpu",type=bool,default=True,help="use gpu or cpu")
    parser.add_argument("--device",type=int,default=0,help="gpu index")

    
    args = parser.parse_args()
    return args