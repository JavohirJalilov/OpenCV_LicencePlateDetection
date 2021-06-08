import matplotlib.pyplot as plt
import numpy as np
import cv2

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False

def show(img,s=8):
    '''
    data visualization
    '''
    plt.figure(figsize=(s,s))
    plt.imshow(img,cmap='gray')
    plt.show()

def get_img(filename):
    '''
    parameter filename.
    return BGR to RGB image
    '''
    img = cv2.imread(filename)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def path_to_list(path)->list:
    '''
    path items to str
    add to list and return
    '''
    path_list = [str(item) for item in path]
    return path_list

def kernal(x,y):
    k = np.ones((x,y),dtype=np.uint8)
    return k

def license_detection(path_list:list)->None:
    img_path = path_list[0]
    img = get_img(img_path)
    mask = cv2.Canny(img,350,500)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal(9,9))
    show(mask)