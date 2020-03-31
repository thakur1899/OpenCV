#thresholding

import cv2
import numpy as np



## Binary Thresholding
# If a pixel value is less than the threshold value then all the pixel values will be converted to zero otherwise to 255.


image = cv2.imread('bookpage.jpg')


def thresholding(image,threshold,max_value=255):
	threshold_image = np.where(image<threshold,0,max_value)  # donot give direct value
	return np.array(threshold_image,dtype = 'uint8')

thresholding_image=thresholding(image,10,255)

grayed_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)


thresholding_image_grayed=thresholding(grayed_image,10,255)

cv2.imshow('image',image)
cv2.imshow('threshold_image',thresholding_image)    #when we give rgb image
cv2.imshow('thresholding_image_grayed',thresholding_image_grayed)    #when we give grayed image.

cv2.waitKey(0)
cv2.destroyAllWindows()
