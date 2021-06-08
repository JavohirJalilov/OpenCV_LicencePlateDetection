import matplotlib.pyplot as plt
import numpy as np
import cv2

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False

def show(img,s=8):
    plt.figure(figsize=(s,s))
    plt.imshow(img,cmap='gray')
    plt.show()

def get_img(name):
    img = cv2.imread(name)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img