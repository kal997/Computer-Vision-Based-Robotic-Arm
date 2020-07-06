import multiprocessing
from inversekinematics import get_angles
from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(500, 2500)
kit.servo[1].set_pulse_width_range(500, 2500)
kit.servo[2].set_pulse_width_range(500, 2500)
kit.servo[3].set_pulse_width_range(500, 2500)
kit.servo[4].set_pulse_width_range(500, 2500)
kit.servo[7].set_pulse_width_range(500, 2500)

def base(ang):
    kit.servo[0].angle = ang


def shoulder(r_ang, l_ang):
    def right_shoulder(ang):
        kit.servo[1].angle = ang
    def left_shoulder(ang): 
        kit.servo[2].angle = ang
    shold_1 = multiprocessing.Process(target= right_shoulder, args=[r_ang])
    shold_2 = multiprocessing.Process(target= left_shoulder, args=[l_ang])
    shold_1.start()
    shold_2.start()
    shold_1.join()
    shold_2.join()
        


def elbow(ang):
    kit.servo[3].angle = ang


def wrist(ang):
    kit.servo[4].angle = ang


def hand(ang):
    kit.servo[7].angle = ang


def pump():
    pass


def move(angles):
    base(angles[0])
    shoulder(angles[1], angles[2])
    elbow(angles[3])
    wrist(angles[4])
    hand(angles[5])



def blue_drop_pos():
    pos = get_angles(10, 0, 5)
    move(pos)


def green_drop_pos():
    pos = get_angles(-10, 0, 5)
    move(pos)


def red_drop_pos():
    
    move(get_angles(-19, 0, 5))


def square_drop_pos():
    pos = get_angles(10, 0, 5)
    move(pos)


def circle_drop_pos():
    pos = get_angles(-10, 0, 5)
    move(pos)


def triangle_drop_pos():
    pos = get_angles(10, 10, 5)
    move(pos)


def parking_pos():
    move([90, 30+140+5, 150-140-5, 180-(-1*-90),0, 40])
    



'''     
blue_drop_pos()
sleep(1)
parking_pos()
sleep(1)
red_drop_pos()
sleep(1)
parking_pos()
sleep(1)
green_drop_pos()
sleep(1)
parking_pos()
'''

'''
move(get_angles(15+0.5, 0, 5))
sleep(5)
shoulder(30+90+5, 150-90-5)
parking_pos()

def sh(x):
    shoulder(30+x+5, 150-x-5)
    
sh(100)
sleep(1)
elbow(180-(-1*-90))
sleep(1)
wrist(90)
'''
'''
def sh(x):
    shoulder(30+x+5, 150-x-5)
elbow(180)
sleep(0.5)
sh(5)
sleep(0.5)
hand(90)
sleep(0.5)
wrist(0)
'''
#move(get_angles(1+10,10, 3))
#print(get_angles(0,14,3))
#parking_pos()
'''
move(get_angles(10,12, 3))
sleep(5)
parking_pos()
sleep(5)
move(get_angles(-22,0, 3))
sleep(5)
parking_pos()
sleep(5)
move(get_angles(-15,15, 3))
sleep(5)
parking_pos()
'''
'''
parking_pos()
sleep(1)
move(get_angles(0-0.5, 22, 3.5))
sleep(5)
'''

#sleep(3)
#move(get_angles(-15, 15, 3))
# positive half x+=1,   y-=0.5 and at x=0
# negative half x-=0.5, y-=0.5 at y=0, y=0






'''
move(get_angles(15, 15, 3))
sleep(10)
parking_pos()
'''