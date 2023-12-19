# any functinality write in a way that it is use in whole application
# LET'S say to savee model in the cloud 

import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle


from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)