import numpy as np
import cv2 as cv


import Student_inherit


img = cv.imread('cc2b.jpg')

print( img.size )
print( img.shape )


# img = np.reshape(img,(10000,17600))

cv.imshow("Image", img)
cv.waitKey()
