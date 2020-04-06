# Transition, Scaling, Kernel, Convolution, Pyramids, Rotational Matrix, Logical Operators (Bitwise Masking)

import numpy as np
import cv2



image = cv2.imread('goku.png')

h, w = image.shape[:2]

# transition_matrix = np.float32([[1, 0, w//4],
# 								[0, 1, h//2]])

# image_transit = cv2.warpAffine(image, transition_matrix, (w, h))

# cv2.imshow('image', image)
# cv2.imshow('image_transit', image_transit)

# transpose_image = cv2.transpose(image)
# cv2.imshow('image', image)
# cv2.imshow('transpose_image', transpose_image)

# rotational_matrix = cv2.getRotationMatrix2D((h/2, w/2), -180, 0.5)bitwise_and(square, ellipse)
# rotational_image = cv2.warpAffine(image, rotational_matrix, (w, h))

# cv2.imshow('image', image)
# cv2.imshow('rotational_matrix', rotational_image)
# bitwise_and(square, ellipse)
# image_scaled_cubic = cv2.resize(image, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_CUBIC)
# image_scaled_area = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
# image_scaled_linear = cv2.resize(image, None, fx=0.15, fy=0.15, interpolation=cv2.INTER_LINEAR)

# cv2.imshow('image_scaled_linear', image_scaled_linear)bitwise_and(square, ellipse)
# cv2.imshow('image_scaled_area', image_scaled_area)bitwise_and(square, ellipse)
# cv2.imshow('image_scaled_cubic', image_scaled_cubic)bitwise_and(square, ellipse)

# smaller = cv2.pyrDown(image)
# larger = cv2.pyrUp(image)



# cv2.imshow('smaller', smaller)
# cv2.imshow('larger', larger)



# Blurring

# kernel_3x3 = np.ones((3, 3), dtype="uint8")
# conved_image = cv2.filter2D(image, -1, kernel_3x3)

# cv2.imshow('image', image)
# cv2.imshow('conved_image', conved_image)


square = np.zeros((300, 300),np.uint8)
cv2.rectangle(square, (80,80), (250, 250), 255, -1)

ellipse = np.zeros((300,300), np.uint8)
cv2.ellipse(ellipse, (100, 100), (100, 100), 30, 0, 180, 255, -1)

And = cv2.bitwise_and(square, ellipse)
Or = cv2.bitwise_or(square, ellipse)
Not = cv2.bitwise_not(square, ellipse)

cv2.imshow('And', And)
cv2.imshow('Or', Or)
cv2.imshow('Not', Not)
cv2.waitKey(0)
