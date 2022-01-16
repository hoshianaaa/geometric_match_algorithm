import cv2
import numpy as np

img = cv2.imread('images/template.jpg', 0)
edges = cv2.Canny(img, 100, 255)

indices = np.where(edges != [0])

# [(x,y), ...]
coordinates = list(zip(indices[1], indices[0])) # zip -> list https://qiita.com/ukisoft/items/bfeb439be673e2df328c

print(coordinates)

x_sum = 0
y_sum = 0
l = len(coordinates)

for i in range(l):
  x_sum = x_sum + coordinates[i][0]
  y_sum = y_sum + coordinates[i][1]

x_center = x_sum / l
y_center = y_sum / l

print(x_center, y_center)

cv2.drawMarker(
    edges, (int(x_center), int(y_center)), color=(255, 0, 0), markerType=cv2.MARKER_TILTED_CROSS, thickness=1
)

cv2.imshow('image',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

