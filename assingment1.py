import cv2
import numpy as np

white_canvas = np.zeros((600,600,3),dtype='uint8')+255
cv2.rectangle(white_canvas,(0,0),(600,200),(0,100,255),-1)
cv2.rectangle(white_canvas,(0,400),(600,600),(0,255,0),-1)
cv2.circle(white_canvas,(300,300),100,(255,0,0),3)
cv2.circle(white_canvas,(300,300),10,(255,0,0),-1)
ci = cv2.circle(white_canvas,(300,300),10,(255,0,0),-1)
cv2.line(white_canvas,(300,400),(300,200),(255,0,0),3)
cv2.line(white_canvas,(400,300),(200,300),(255,0,0),3)
cv2.line(white_canvas,(230,230),(370,370),(255,0,0),3)
cv2.line(white_canvas,(230,370),(370,230),(255,0,0),3)

# cv2.line(white_canvas,(250,215),(350,340),(255,0,0),3)
# cv2.line(white_canvas,(270,200),(300,300),(255,0,0),3)







# m=cv2.getRotationMatrix2D((300,300),15,1)

# dd  = cv2.warpAffine(ci,m,(300,300))

cv2.imshow('white_canvas',white_canvas)


video_cap = cv2.VideoCapture(0)


while True:
	_,frame = video_cap.read()
	frame = cv2.resize(frame,(600,600))
	frame = cv2.flip(frame,1)

	# frame_add = frame+img2_resize

	assert frame.shape == white_canvas.shape, "Image shape not equal"

	frame_add = cv2.addWeighted(frame,0.80,white_canvas,0.60,0)

	cv2.imshow('frame_add',frame_add)
	cv2.imwrite('frame_flag.jpg',frame_add)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break

video_cap.release()

# cv2.waitKey(0)
cv2.destroyAllWindows()