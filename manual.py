import cv2
c=0
d=0

def click_event(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img,(x,y),3,(0,0,255),-1)
		cv2.imshow('image',img)
		global c
		c=c+1
	if event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(img,(x,y),3,(255,255,0),-1)
		cv2.imshow('image',img)
		c=c-1
		global d
		d=d+1


		
img =cv2.imread('crop1.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
		
cv2.waitKey(0)
cv2.destroyAllWindows()
print(c)
print(d)
