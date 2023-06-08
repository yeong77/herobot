import os
import math
import cv2
from imutils.video import VideoStream

#img = cv2.imread('/home/yy/shape_detect/shape.png')
#vs = VideoStream(src=0).start()
#vs=cv2.VideoCapture(0,cv2.CAP_V4L) 
ratio = 0


def setLabel(cap, pts, label):
	(x, y, w, h) = cv2.boundingRect(pts)
	pt1 = (x, y)
	pt2 = (x + w, y + h)
	cv2.rectangle(cap, pt1, pt2, (0, 255, 0), 2)
	cv2.putText(cap,label, (pt1[0], pt1[1]-3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
	

 


while cv2.waitKey(33) < 0:
	cap = cv2.VideoCapture(2)
	ret, cap = cap.read()
	
	gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

	ret, thr = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

	contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

	for cont in contours:
		approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
		vtc = len(approx)
	
		if vtc == 4:
			setLabel(cap, cont, 'Rec')
			cv2.imshow('img', cap)
			cv2.imshow('binary', thr)
		
		else:
			pass
			
	

cap.release()
cv2.destroyAllWindows()



