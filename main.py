import matplotlib.pyplot as plt
import numpy as np
import cv2
import pathlib

import func
from func import show, get_img

# pip install -r requirements.txt git

path_images = pathlib.Path('CAR_IMG_600X600').iterdir()

path_list = func.path_to_list(path_images)
print(path_list)