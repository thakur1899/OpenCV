import cv2
import numpy as np

# black_canvas = np.zeros((400,400,3),dtype='uint8')
# white_canvas = np.zeros((400,400,3),dtype='uint8')+255


#cv2.line(white_canvas,(0,0),(400,400),(0,0,255),3)

# zeros = np.zeros(white_canvas.shape[:2],dtype='uint8')

# b,g,r=cv2.split(white_canvas)

# new_canvas = cv2.merge([b,zeros,zeros])



video_cap = cv2.VideoCapture(0)

while True:
	ret,frame = video_cap.read()
	frame=cv2.flip(frame,1)

	zeros = np.zeros(frame.shape[:2],dtype='uint8')

	b,g,r=cv2.split(frame)

	blue_canvas = cv2.merge([b,zeros,zeros])


	cv2.imshow('frame',frame)
	cv2.imwrite('frame.jpg',frame)
	if cv2.waitKey(1) & 0xff == ord('w'):
		break
video_cap.release()
cv2.destroyAllWindows()


#cv2.imshow('black_canvas',black_canvas)
#cv2.imshow('white_canvas',white_canvas)

# cv2.imshow('blue_canvas',new_canvas)

# cv2.waitKey(0)
# cv2.destroyAllWindows()