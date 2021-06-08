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

def max_area_idx(contours):
    area_list = []
    for i in range(len(contours)):
        area_list.append(cv2.contourArea(contours[i]))
    area_list = np.array(area_list)
    mx_idx = area_list.argmax()
    return mx_idx

def license_detection(path_list:list)->None:
    img_path = path_list[0]
    img = get_img(img_path)
    mask = cv2.Canny(img,350,500)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal(9,9))
    mask = cv2.dilate(mask,kernal(5,5))
    mask = cv2.erode(mask,kernal(6,6))

    contours,_ =cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    mx_idx = max_area_idx(contours)
    x,y,w,h = cv2.boundingRect(contours[mx_idx])
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imwrite('detect_license.png',cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    show(img)