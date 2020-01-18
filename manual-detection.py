import cv2
c=0
d=0
e=0

def click_event(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:              #for normal chromosomes
		cv2.circle(img,(x,y),3,(0,0,255),-1)
		cv2.imshow('image',img)
		global c
		c=c+1

	if event == cv2.EVENT_RBUTTONDOWN:              #for dicentric chromosomes
		cv2.circle(img,(x,y),3,(255,255,0),-1)
		cv2.imshow('image',img)
		global d
		d=d+1

	if event == cv2.EVENT_LBUTTONDBLCLK:             #for collided chromosomes 
         cv2.circle(img,(x,y),3,(255,0,0),-1)
         global e
         e=e+1

         

img =cv2.imread('cro2.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
		
cv2.waitKey(0)
cv2.destroyAllWindows()
print("no of normal chromosomes")
print(c)
print("no of dicentric chromosomes")
print(d)
print("no of collided chromosomes")
print(e)
print("total no of segments")
print(c+d+e)
