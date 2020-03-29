import cv2
import  numpy as np

img = cv2.imread('goku.png')


# cap = cv2.VideoCapture(0)
# while True:
# 	_, frame = cap.read()
# 	cv2.imshow('frame', frame)

# 	if cv2.waitKey(1) & 0xff == ord('q'):
# 		break

print(img.shape)
print(type(img))
print(img.max())
print(img.min())
print(img.transpose().shape)
cv2.imshow('goku',img)




grayed_img = cv2.imread('goku.png',0)
cv2.imshow('grayed_img',grayed_img)


print(img.ndim)
print(grayed_img.ndim)




b ,g ,r = cv2.split(img)
new_img = cv2.merge([b, g, r])

amp_img = cv2.merge([b ,g+50, r])

cv2.imshow('merged_img',new_img)
cv2.imshow('amplified image',amp_img)


crop_image = img[200:400]
cv2.imshow('crop_image',crop_image)

cv2.waitKey(0)

#cap.release()
#cv2.destroyAllWindows()