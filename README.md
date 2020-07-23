# Computer Vision Based Robotic Arm.  

The algorithm starts with image acquisition stage, in which we specify image properties such as resolution. Then the 
image is saved to specific directory. The image name is then concatenated with the round number (round is the algorithm 
execution for one time) for example `img_1.jpg`, note that round number is variable that is been updated every single 
shot.  
Then we read the image from this specified directory and apply smoothing filter to eliminate the unwanted noise and background edges. After smoothing the image, it will be ready for color segmentation stage, in this stage we transform the color model of the captured image from RGB(red, green and blue) model to HSV(hue, saturation and value) model. Then according to user’s HSV upper and lower limit values, we will check for every pixel that it is within the specified range using `cv2.inRange` function. The resulting image will be binary image with black background and white foreground (which represents the detected objects and a little small white dots and lines which are detected noise).  
This binary image will be passed to `cv2.findContours` function which returns the detected contours and its geometrical properties. We then apply threshold
based on the contours area to eliminate the noise contours, after that we will end up with the objects contours and it’s geometrical properties such as area in pixels and the center of the contour in pixels relative to the camera frame. Then we apply pixels to centimeters conversion and transform these object’s (x, y) coordinates from the camera frame to the robot base frame.  
After these conversions, these coordinates are appended to list and returned with the raw colored image with drawn contours from `detection.ObjectDetection.color` method, then the coordinates are ready to be sent to the kinematics equations. We then pass the first element in the coordinates list to the `inversekinematics.get_angles` function, this function returns the corresponding angles that positions the robot’s end effector in the required (x, y) location using forward and inverse kinematics equations. Then the returned angles will be passed to the `modified_joints.move` function, this function sends every joint angle to the corresponding joint motor, the result will be positioning the end effector in the required location (the object’s location). Then the vacuum pump will be turned on using `modified_joints.pump` (1 for ON, 0 for OFF), the suction cup which is the end effector will suck the object and then the arm will move to the corresponding drop position for the detected color, then the pump will be turned off and the object will be dropped in the desired location.  
As we execute more rounds, the object’s number will be decreased by 1 every single round. After gripping the very last object, the workspace will be clean this means that there are no objects to grip, so we will break the main loop and end the program. The algorithm flowchart is shown below.  
![algo](https://drive.google.com/file/d/1RIPlzv1YpoGCY6HA4tkimFrYlaqIvo1V/view?usp=sharing "algo")  
 
The robot code is divided into five modules, one calibration file and main file. We will
discuss in the next section the the contents of every file in the next section.

**inversekinematics.py** module has `get_angles` function that holds the model
configuration parameters, forward kinematics equations and inverse kinematics
equations. This function takes the desired end effector position in Cartesian
coordinates and its orientation and it returns the corresponding 6 joints angles in
degrees as a list.  

**detection.py** module has `ObjectDetection` class that has three class object
attributes which are `lower_hsv`, `upper_hsv` and threshold contour pixel area `cnt_area`. The
class also has two method which are `ObjectDetection.color` and
`ObjectDetection.shape`, both of the methods takes a BGR image and returns a
list that contains the coordinates of the detected objects, binary image shows the
detected objects and raw input image with drawn detected contours.  

**modified_joints.py** module contains the motor’s control functions. Every joint
has its own function such as `base`, `shoulder`, `elbow`, `wrist`, `hand`, and `pump`.
Every function takes the desired angle in degrees, except pump function which
takes one for on and zero for off. There is also `move` function which takes a list of angles and passes each angle to the corresponding joint. There are parking positions functions, one for each color and shape such as `circle_drop_pos()` and one for idle position `parking_pos`.  

**gui.py** has the `user_input` function which displays GUI from which the user has
to choose which object he wishes to sort. This function returns six flags, one flag
for each sorting option such as green, red, blue, circular, triangular, and squared. the returned flags have one `True` and the other five are `False`. The returned `True` flag will execute only the corresponding `while` loop in main.  

**hsv_calibration.py** is used to specify the upper and lower values for hue, value,
and saturation for specific color. The user has to use the track-bars to choose
appropriate ranges that give satisfying results. These limits are printed as an array
and then it will be ready to be passed as an arguments to create a new `detection.ObjectDetection` instance in `main.py`.  

**main.py** is the main file in the project that imports all of the modules and its
functions. It has six while loops, one loop for each sorting option. According to
the user’s input, the corresponding flag will be returned as `True` and the rest as
`False`. As a result, the corresponding while loop will be executed and the
rest will be skipped. Each loop has the round algorithm as we mentioned above in
the previous section. After we break the loop after finishing. Sorting process have done successfully will be printed as a feedback and the
program will end.  
