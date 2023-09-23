from pickletools import uint8
import cv2 as np    
import cv2
from numpy import dtype
print (cv2.__version__)
im= np.zeos( (300,300,3), dtype= np.uint8)

cv2.imshow("prueba",im)
cv2.waitKey(0)