import cv2
import numpy as np

class ObjectDetection:
    """
    The ObjectDetection class contains two detection method which are color  and shape detection, each one of them
    has its own attributes
    This class also has one class variable -- font
    """

    def __init__(self, lower_hsv, upper_hsv, cnt_area):
        """
        The init method attributes are:
        :param lower_hsv: array contains the lower Hue, Saturation and Values for a specific color
        :param upper_hsv: array contains the upper Hue, Saturation and Values for a specific color
        :param cnt_area: will act as threshold value to eliminate the noise from the detected contours
        """
        self.lower_hsv = lower_hsv
        self.upper_hsv = upper_hsv
        self.cnt_area = cnt_area

    def color(self, img):
        """
        Color detection method based on masking lower and upper hsv array to BGR image
        :param img: BGR image
        :return: coordinates: list contains the cartesian coordinates of the detected objects
                 mask: Binary image contains all the detected contours
                 img: input image copy with drawn contours, centers and (x,y) coordinates
        """
        font = cv2.FONT_HERSHEY_COMPLEX
        img = cv2.medianBlur(img, 5)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img, self.lower_hsv, self.upper_hsv)

        coordinates = []
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > self.cnt_area:
                cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)
                M = cv2.moments(contour)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # (x, y) relative to camera frame
                cXX = cX / 22.260         # 39.3700787) + 0.5)
                cYY = cY / 21.6         # 39.3700787) + 0.5)

                robot_frame = np.dot(np.array([[-1, 0, 0, 580/22.260], [0, 1, 0, 45/21.6], [0, 0, -1, 0], [0, 0, 0, 1]]),
                                     np.array([[cXX], [cYY], [0], [1]]))
                # (x, y) relative to robot frame
                cXX = float("{0:.2f}".format(robot_frame[0, 0]))
                cYY = float("{0:.2f}".format(robot_frame[1, 0]))
                cYY -= 4

                cv2.putText(img, f"({cXX},{cYY})", (cX + 5, cY + 5), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.circle(img, (cX, cY), 3, (0, 0, 255), -1)
                coordinates.append(tuple((cXX, cYY, 6)))
            else:
                continue

        return coordinates, mask, img

    def shape(self, img):
        """
        Shape detection method based on masking lower and upper hsv array to BGR image
        :param img: BGR image
        :return: (triangles_coordinates, triangles_img): list contains the cartesian coordinates of the detected
        triangular objects, input image copy with drawn contours, centers and (x,y) coordinates of triangular objects)
        (squares_coordinates, squares_img): list contains the cartesian coordinates of the detected squared
        objects, input image copy with drawn contours, centers and (x,y) coordinates of squares objects)
        (circles_coordinates, circles_img): list contains the cartesian coordinates of the detected
        circular objects, input image copy with drawn contours, centers and (x,y) coordinates of circular objects)
        """
        def contour_center(cnt):
            """
            :param cnt: contour array
            :return: (cXX, cYY): cartesian coordinates in cm
                     (cX, cY): pixel coordinates
            """

            M = cv2.moments(cnt)
            cX = int(M["m10"] / M["m00"])  # cX is the x coordinate in pixels
            cY = int(M["m01"] / M["m00"])  # cY is the y coordinate in pixels

            # (x, y) relative to camera frame
            cXX = cX / 22.2  # 39.3700787) + 0.5)
            cYY = cY / 21.6  # 39.3700787) + 0.5)

            robot_frame = np.dot(np.array([[-1, 0, 0, 580/22.260], [0, 1, 0, 45/21.6], [0, 0, -1, 0], [0, 0, 0, 1]]),
                                     np.array([[cXX], [cYY], [0], [1]]))
            # (x, y) relative to robot frame
            cXX = float("{0:.2f}".format(robot_frame[0, 0]))
            cYY = float("{0:.2f}".format(robot_frame[1, 0]))
            return tuple((cXX, cYY)), tuple((cX, cY))  # coordinates in cm, coordinates in pixels

        font = cv2.FONT_HERSHEY_COMPLEX
        img = cv2.medianBlur(img, 5)
        triangles_img = img.copy()
        squares_img = img.copy()
        circles_img = img.copy()
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img, self.lower_hsv, self.upper_hsv)

        squares_coordinates = []
        triangles_coordinates = []
        circles_coordinates = []

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > self.cnt_area:  # 3shan afsl el noise
                approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
                # the length of the approx hayt3'yr 3ala 7asab bo3d el object
                # 3an el camera we brdo el constant el mdrob fe arclength
                if len(approx) == 3:
                    cv2.drawContours(triangles_img, [approx], -1, (0, 0, 255), 3)
                    (cxx, cyy), (cx, cy) = contour_center(contour)
                    cv2.putText(triangles_img, f"({cxx},{cyy})", (cx + 5, cy + 5), font, 0.5, (
                        0, 0, 255), 1, cv2.LINE_AA)
                    cv2.circle(triangles_img, (cx, cy), 3, (0, 0, 255), -1)
                    triangles_coordinates.append(tuple((cxx, cyy)))

                elif len(approx) == 4:
                    cv2.drawContours(squares_img, [approx], -1, (0, 255, 0), 3)
                    (cxx, cyy), (cx, cy) = contour_center(contour)
                    cv2.putText(squares_img, f"({cxx},{cyy})", (cx + 5, cy + 5), font, 0.5, (
                        0, 0, 255), 1, cv2.LINE_AA)
                    cv2.circle(squares_img, (cx, cy), 3, (0, 0, 255), -1)
                    squares_coordinates.append(tuple((cxx, cyy)))

                elif len(approx) == 8:
                    cv2.drawContours(circles_img, [approx], -1, (255, 0, 0), 3)
                    (cxx, cyy), (cx, cy) = contour_center(contour)
                    cv2.putText(circles_img, f"({cxx},{cyy})", (cx + 5, cy + 5), font,
                                0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.circle(circles_img, (cx, cy), 3, (0, 0, 255), -1)
                    circles_coordinates.append(tuple((cxx, cyy)))

                else:
                    continue
        return (triangles_coordinates, triangles_img), (squares_coordinates, squares_img
                                                        ), (circles_coordinates, circles_img)
