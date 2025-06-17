import os
import argparse
import torch
import random
import numpy as np
from config.config import get_config,set_seed
from pipe.trainer import Trainer
from pipe.inference import Inference

if __name__ == "__main__":
    
    args = get_config()
    set_seed(args.seed)

    
    if args.training:
        
        # Init wandb
        
        trainer = Trainer(args)
        trainer.train()
    else:
        inference = Inference(args)
        inference.inference()