import cv2
import numpy as np

img1 = cv2.imread('dog.png')

img1 = cv2.resize(img1,(800,800))


video_cap = cv2.VideoCapture(0)


while True:
	_,frame = video_cap.read()
	frame = cv2.resize(frame,(800,800))
	frame = cv2.flip(frame,1)

	# frame_add = frame+img2_resize

	frame_add = cv2.addWeighted(frame,0.80,img1,0.80,0)

	cv2.imshow('frame_add',frame_add)
	cv2.imwrite('VideoCapture.jpg',frame_add)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break

video_cap.release()
cv2.destroyAllWindows()

