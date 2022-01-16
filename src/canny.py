import cv2
import numpy as np

img = cv2.imread('images/template.jpg', 0)
edges = cv2.Canny(img, 100, 255)

w,h = edges.shape

for i in range(w):
  for j in range(h):
#    print(i,j,edges[i,j])
    if (edges[i,j] > 0):
      cv2.circle(edges, (j, i), 10, 0, thickness=-1)
      edges[i,j] = 255

cv2.imshow("edges",edges)
cv2.waitKey(0)
