import cv2
import numpy as np

img = cv2.imread('images/template.jpg', 0)
edges = cv2.Canny(img, 100, 255)

indices = np.where(edges != [0])
coordinates = list(zip(indices[0], indices[1])) # zip -> list https://qiita.com/ukisoft/items/bfeb439be673e2df328c

print(coordinates)

x_sum = 0
y_sum = 0
l = len(coordinates)

for i in range(l):
  x_sum = x_sum + coordinates[i][1]
  y_sum = y_sum + coordinates[i][0]

x_center = x_sum / l
y_center = y_sum / l

print(x_center, y_center)

cv2.drawMarker(
    edges, (int(x_center), int(y_center)), color=(255, 0, 0), markerType=cv2.MARKER_TILTED_CROSS, thickness=1
)

tf_coordinates = []

for i in range(l):
  tf_coordinates.append((coordinates[i][0] - x_center, coordinates[i][1] - y_center))

print(tf_coordinates)

s = cv2.imread('images/search1.jpg', 0)
s2 = cv2.imread('images/search2.jpg', 0)

se = cv2.Canny(s, 100, 255)
se2 = cv2.Canny(s2, 100, 255)


height = 300
width = 600

while True:
  for i in range(width):
    for j in range(height):

      x = i % width
      y = j % height

      blank = np.zeros((height, width, 1))

      for k in range(len(tf_coordinates)):
        px = int(tf_coordinates[k][0] + x)
        py = int(tf_coordinates[k][1] + y)
        if (px >= 0 and px <= width):
          if (py >= 0 and py <= height):
            blank[px,py,0] = 255

      cv2.imshow('image',edges)
      cv2.imshow('s',s)
      cv2.imshow('s2',s2)
      cv2.imshow('se',se)
      cv2.imshow('se2',se2)
      cv2.imshow('blank',blank)
      cv2.waitKey(1)

cv2.destroyAllWindows()



