import cv2
import numpy as np
from time import sleep
from picamera import PiCamera
from detection import ObjectDetection
from gui import user_input
from inversekinematics import get_angles            # importing kinematics equations
import modified_joints                              # importing motors functions
number = 1                                          # initial no. to start with capturing function

camera = PiCamera()
camera.resolution = (1024, 768)
triangles_check, squares_check, circles_check, red_check, green_check, blue_check = user_input()


# To create an instance of the class depends on the user input

if triangles_check or squares_check or circles_check:
    detected_shape = ObjectDetection(np.array([0, 121, 26]), np.array([180, 255, 255]), 2000)
elif green_check:
    green_color = ObjectDetection(np.array([65,138,65]), np.array([98,233,193]), 2000)
elif red_check:
    red_color = ObjectDetection(np.array([0,90,90]), np.array([180,174,132]), 2000)
elif blue_check:
    blue_color = ObjectDetection(np.array([103,139,27]), np.array([157,220,153]), 2000)

while red_check:
    
    camera.start_preview()
    sleep(2)
    camera.capture(f'/home/pi/Desktop/images/img{number}.jpg')
    camera.stop_preview()
    pic = cv2.imread(f'/home/pi/Desktop/images/img{number}.jpg')
    red_coors, red_mask, red_img = red_color.color(img=pic)
    if len(red_coors) == 0:
        red_check = False
        print("There are no red objects left!")
        cv2.namedWindow("red img", cv2.WINDOW_AUTOSIZE)
        # cv2.namedWindow("red mask", cv2.WINDOW_AUTOSIZE)
        # cv2.moveWindow("red mask", int(pic.shape[1]),0)
        cv2.moveWindow("red img", 0,0)
        # cv2.imshow("red mask", red_mask)
        cv2.imshow("red img", red_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

    else:
        print(f"The current red detected objects are at : {red_coors}")
        cv2.namedWindow("red img", cv2.WINDOW_AUTOSIZE)
        # cv2.namedWindow("red mask", cv2.WINDOW_AUTOSIZE)
        # cv2.moveWindow("red mask", int(pic.shape[1]), 0)
        cv2.moveWindow("red img", 0, 0)
        # cv2.imshow("red mask", red_mask)
        cv2.imshow("red img", red_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        number += 1     # to rename the next captured image
        modified_joints.move(get_angles(red_coors[0][0], red_coors[0][1], red_coors[0][2]))
        sleep(2)
        # joints.pump()       # turn on the pump
        joints.red_drop_pos()
        sleep(2)
        # joints.pump()       # turn of the pump
        modified_joints.parking_pos()

while green_check:
    camera.start_preview()
    sleep(2)
    camera.capture(f'/home/pi/Desktop/images/img{number}.jpg')
    camera.stop_preview()
    pic = cv2.imread(f'/home/pi/Desktop/images/img{number}.jpg')
    green_coors, green_mask, green_img = green_color.color(pic)
    if len(green_coors) == 0:
        green_check = False
        print("There are no green objects left!")
        cv2.namedWindow("green img", cv2.WINDOW_AUTOSIZE)
        # cv2.namedWindow("green mask", cv2.WINDOW_AUTOSIZE)
        # cv2.moveWindow("green mask", int(pic.shape[1]), 0)
        cv2.moveWindow("green img", 0, 0)
        # cv2.imshow("green mask", green_mask)
        cv2.imshow("green img", green_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

    else:
        print(f"The current green detected objects are at : {green_coors}")
        cv2.namedWindow("green img", cv2.WINDOW_AUTOSIZE)
        # cv2.namedWindow("green mask", cv2.WINDOW_AUTOSIZE)
        # cv2.moveWindow("green mask", int(pic.shape[1]), 0)
        cv2.moveWindow("green img", 0, 0)
        # cv2.imshow("green mask", green_mask)
        cv2.imshow("green img", green_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        number += 1                         # to rename the next captured image
        modified_joints.move(get_angles(green_coors[0][0], green_coors[0][1], green_coors[0][2]))
        sleep(2)
        # joints.pump()  # turn on the pump
        modified_joints.green_drop_pos()
        sleep(2)
        # joints.pump()  # turn of the pump
        modified_joints.parking_pos()
while blue_check:
    camera.start_preview()
    sleep(2)
    camera.capture(f'/home/pi/Desktop/images/img{number}.jpg')
    camera.stop_preview()
    pic = cv2.imread(f'/home/pi/Desktop/images/img{number}.jpg')
    blue_coors, blue_mask, blue_img = blue_color.color(pic)
    if len(blue_coors) == 0:
        blue_check = False
        print("There are no blue objects left!")
        cv2.namedWindow("blue img", cv2.WINDOW_AUTOSIZE)
        # cv2.namedWindow("blue mask", cv2.WINDOW_AUTOSIZE)
        # cv2.moveWindow("blue mask", int(pic.shape[1]), 0)
        cv2.moveWindow("blue img", 0, 0)
        # cv2.imshow("blue mask", blue_mask)
        cv2.imshow("blue img", blue_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
    else:
        print(f"The current blue detected objects are at : {blue_coors}")
        cv2.namedWindow("blue img", cv2.WINDOW_AUTOSIZE)
        # cv2.namedWindow("blue mask", cv2.WINDOW_AUTOSIZE)
        # cv2.moveWindow("blue mask", int(pic.shape[1]), 0)
        cv2.moveWindow("blue img", 0, 0)
        # cv2.imshow("blue mask", blue_mask)
        cv2.imshow("blue img", blue_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        number += 1
        modified_joints.move(get_angles(blue_coors[0][0], blue_coors[0][1], blue_coors[0][2]))
        sleep(2)
        # joints.pump()  # turn on the pump
        modified_joints.blue_drop_pos()
        sleep(2)
        # joints.pump()  # turn of the pump
        modified_joints.parking_pos()

number = 1
while squares_check:
    pic = cv2.imread(f"C:\\Users\\KHALED\\Desktop\\pics\\{number}.jpg")
    # pic = cv2.resize(pic, (int(pic.shape[1] / 2), int(pic.shape[0] / 2)))
    (triangles_coors,triangles_img),(squares_coors,squares_img),(circles_coors,circles_img) = detected_shape.shape(pic)
    if len(squares_coors) == 0:
        squares_flag = False
        print("there are no squared objects left!")
        cv2.namedWindow("squares", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("squares", 0, 0)
        cv2.imshow("squares", squares_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        break
    else:
        print(f"The current squared detected objects are at : {squares_coors}")
        cv2.namedWindow("squares", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("squares", 0, 0)
        cv2.imshow("squares", squares_img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        number += 1
        angles = get_angles(squares_coors[0])
        joints.move(angles)
        joints.pump()  # turn on the pump
        joints.square_drop_pos()
        joints.pump()  # turn of the pump
        joints.parking_pos()

number = 3  # will be removed
while triangles_check:
    pic = cv2.imread(f"C:\\Users\\KHALED\\Desktop\\pics\\{number}.jpg")
    # pic = cv2.resize(pic, (int(pic.shape[1] / 2), int(pic.shape[0] / 2)))
    (triangles_coors,triangles_img),(squares_coors,squares_img),(circles_coors,circles_img) = detected_shape.shape(pic)
    if len(triangles_coors) == 0:
        triangles_flag = False
        print("there are no triangular detected objects left!")
        cv2.namedWindow("triangles", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("triangles", 0, 0)
        cv2.imshow("triangles", triangles_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        break
    else:
        print(f"The current triangular detected objects are at : {triangles_coors}")
        cv2.namedWindow("triangles", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("triangles", 0, 0)
        cv2.imshow("triangles", triangles_img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        number += 1
        angles = get_angles(triangles_coors[0])
        joints.move(angles)
        joints.pump()  # turn on the pump
        joints.triangle_drop_pos()
        joints.pump()  # turn of the pump
        joints.parking_pos()


number = 4  # will be removed
while circles_check:
    pic = cv2.imread(f"C:\\Users\\KHALED\\Desktop\\pics\\{number}.jpg")
    # pic = cv2.resize(pic, (int(pic.shape[1] / 2), int(pic.shape[0] / 2)))
    (triangles_coors,triangles_img),(squares_coors,squares_img),(circles_coors,circles_img) = detected_shape.shape(pic)
    if len(circles_coors) == 0:
        circles_flag = False
        print("there are no circular objects left!")
        cv2.namedWindow("circles", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("circles", 0, 0)
        cv2.imshow("circles", circles_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        break
    else:
        print(f"The current circular detected objects are at : {circles_coors}")
        cv2.namedWindow("circles", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("circles", 0, 0)
        cv2.imshow("circles", circles_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        number += 1
        angles = get_angles(circles_coors[0])
        joints.move(angles)
        joints.pump()  # turn on the pump
        joints.circle_drop_pos()
        joints.pump()  # turn of the pump
        joints.parking_pos()
print("Sorting process have done successfully.")
cv2.waitKey(100)
cv2.destroyAllWindows()
