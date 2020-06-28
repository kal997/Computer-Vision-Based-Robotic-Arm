import multiprocessing
from inversekinematics import get_angles
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(500, 2500)
kit.servo[1].set_pulse_width_range(500, 2500)
kit.servo[2].set_pulse_width_range(500, 2500)
kit.servo[3].set_pulse_width_range(500, 2500)
kit.servo[4].set_pulse_width_range(500, 2500)
kit.servo[5].set_pulse_width_range(500, 2500)

"""
With a standard servo, you specify the position as an angle. The angle will always be between 0 and the actuation range.
The default is 180 degrees but your servo may have a smaller sweep. You can change the total angle by setting actuation
range.

For example, to set the actuation range to 160 degrees:
kit.servo[0].actuation_range = 160
"""
"""
Often the range an individual servo recognises varies a bit from other servos. If the servo didn't sweep the full
expected range, then try adjusting the minimum and maximum pulse widths using 
set_pulse_width_range(min_pulse, max_pulse).

To set the pulse width range to a minimum of 1000 and a maximum of 2000:
kit.servo[0].set_pulse_width_range(1000, 2000)
"""


def base(ang):
    kit.servo[0].angle = ang


def shoulder_no1(ang):
    kit.servo[1].angle = ang


def shoulder_no2(ang):
    kit.servo[2].angle = ang


def elbow(ang):
    kit.servo[3].angle = ang


def wrist(ang):
    kit.servo[4].angle = ang


def hand(ang):
    kit.servo[5].angle = ang


def pump():
    pass


def move(angles):
    base(angles[0])
    shoulder_no1(angles[1])
    shoulder_no2(angles[2])
    elbow(angles[3])
    wrist(angles[4])
    hand(angles[5])


def blue_drop_pos():
    pos = get_angles(6, 0, 5)
    move(pos)


def green_drop_pos():
    pos = get_angles(10, 0, 5)
    move(pos)


def red_drop_pos():
    pos = get_angles(-6, 0, 5)
    move(pos)


def square_drop_pos():
    pos = get_angles(6, 0, 5)
    move(pos)


def circle_drop_pos():
    pos = get_angles(10, 0, 5)
    move(pos)


def triangle_drop_pos():
    pos = get_angles(-6, 0, 5)
    move(pos)


def parking_pos():
    move([90, 120+30+5, (150-120)-5, 180-(-1*-90), 10, 0])
    
    


parking_pos()
blue_drop_pos()
base(45)


