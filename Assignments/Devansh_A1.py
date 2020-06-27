import numpy as np
import cv2
x=[] 
y=[]
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (3, 3)) 
    
    # Apply Hough transform(there's a good document that explains that) on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,param2 = 30, minRadius = 30, maxRadius = 40)
    # Draw circles that are detected. 
    if detected_circles is not None: 
    
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
    
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2]
            x.append(a)
            y.append(b)
            # Draw the circumference of the circle. 
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
    
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
            # cv2.line(frame, (a,b), (c,d), (0, 0, 255), 2)

            
            cv2.imshow("Detected Circle", frame) 
    for i in range(len(x)):
        cv2.line(frame, (x[i-1],y[i-1]), (x[i],y[i]), (0, 0, 255), 2)
    cv2.imshow("Detected Circle", frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()