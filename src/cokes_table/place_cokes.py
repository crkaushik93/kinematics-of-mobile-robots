#! /usr/bin/env python

import math, rospy
from tf.transformations import quaternion_about_axis, quaternion_multiply
from utilities import set_model_state
from geometry_msgs.msg import Pose, Point, Quaternion

position = Point(1,0,0)
q = quaternion_about_axis(math.radians(90), (0,0,1))
orientation = Quaternion(*q)
set_model_state('table', Pose(position, orientation))


for angle in range(0,360,30):
    can = angle/30
    print("can angle", can)
    theta = math.radians(angle)
    print("theta", theta)
    xp = 0.2 * math.cos(theta) + 1
    print("xp", xp)
    yp = 0.2 * math.sin(theta)
    print("yp", yp)
    model_name = 'coke_can_' + str(can)
    position = Point(xp,yp,1.05)
    print("position", position)
    q_z = quaternion_about_axis(theta, (0,0,1))
    q_y = quaternion_about_axis(math.radians(90), (0,1,0))
    q_zy = quaternion_multiply(q_z, q_y)
    orientation = Quaternion(*q_zy)
    set_model_state(model_name, Pose(position, Quaternion(*q_zy)))
    rospy.sleep(0.1)