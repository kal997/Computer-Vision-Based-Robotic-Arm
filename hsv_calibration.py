import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
    


cv2.namedWindow("TRACKBARS")
cv2.createTrackbar("L_H","TRACKBARS",0,180,nothing)
cv2.createTrackbar("L_S","TRACKBARS",0,255,nothing)
cv2.createTrackbar("L_V","TRACKBARS",0,255,nothing)
cv2.createTrackbar("U_H","TRACKBARS",0,180,nothing)
cv2.createTrackbar("U_S","TRACKBARS",0,255,nothing)
cv2.createTrackbar("U_V","TRACKBARS",0,255,nothing)

while True:
    _, frame = cap.read()
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L_H","TRACKBARS")
    l_s = cv2.getTrackbarPos("L_S","TRACKBARS")
    l_v = cv2.getTrackbarPos("L_V","TRACKBARS")
    u_h = cv2.getTrackbarPos("U_H","TRACKBARS")
    u_s = cv2.getTrackbarPos("U_S","TRACKBARS")
    u_v = cv2.getTrackbarPos("U_V","TRACKBARS")
    lower_value = np.array([l_h,l_s,l_v])
    upper_value = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv_img,lower_value,upper_value)
    cv2.imshow("masked img",mask)
    cv2.imshow("img",frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
print(f"lower = [{l_h},{l_s},{l_v}]")
print(f"upper = [{u_h},{u_s},{u_v}]")

cap.release()
cv2.destroyAllWindows()