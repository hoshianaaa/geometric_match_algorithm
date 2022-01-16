import cv2
import numpy as np
 
#ブランク画像
height = 300
width = 400
blank = np.zeros((height, width, 1))
 
cv2.imshow('blank',blank)
cv2.waitKey(0)
