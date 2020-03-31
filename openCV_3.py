import cv2
import numpy as np

img1 = cv2.imread('goku.png')
img2 = cv2.imread('strom.jpg')

# cv2.imshow('goku',img1)
# cv2.imshow('mickey',img2)

print(img2.shape)
print(img2.shape)

img1_resize = cv2.resize(img1,(400,400))
img2_resize = cv2.resize(img2,(400,400))



#print(help(cv2.resize))

assert img1_resize.shape == img2_resize.shape, "Image shape not equal"

img = img1_resize+img2_resize

cv2.imshow("resized_image1",img1_resize)
cv2.imshow("resized_image2",img2_resize)
cv2.imshow("Added_Image",img)

video_cap = cv2.VideoCapture(0)


while True:
	_,frame = video_cap.read()
	frame = cv2.resize(frame,(400,400))
	frame = cv2.flip(frame,1)

	# frame_add = frame+img2_resize

	frame_add = cv2.addWeighted(frame,0.80,img2_resize,0.60,0)

	cv2.imshow('frame_add',frame_add)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break

video_cap.release()
cv2.destroyAllWindows()


# cv2.waitKey(0)
# cv2.destroyAllWindows()

