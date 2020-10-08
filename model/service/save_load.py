import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf
import util.version_checker

class SaveLoad:

    train_images : object = None
    train_labels : object = None
    test_images : object = None
    test_labels : object = None
    
    def __init__(self):
        util.version_checker.env_info()

    def hook(self):
        pass