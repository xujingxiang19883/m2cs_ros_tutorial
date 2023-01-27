#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from m2_ps4.msg import Ps4Data
# hint: some imports are missing

old_data = Ps4Data()

def callback(data: Ps4Data):
    global old_data

    # you should publish the velocity here!
    pos = Twist()
    pos.linear.x = data.hat_ly
    pos.angular.z = data.hat_rx
    pub.publish(pos)
    # hint: to detect a button being pressed, you can use the following pseudocode:
    # if ((data.button is pressed) and (old_data.button not pressed)),
    # then do something...

    old_data = data

if __name__ == '__main__':
    rospy.init_node('ps4_controller')
    
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size = 1)
    # publisher object goes here... hint: the topic type is Twist
    sub = rospy.Subscriber("/input/ps4_data",Ps4Data,callback,queue_size = 1)# subscriber object goes here
    
    # one service object is needed for each service called!
    # srv_col = rospy.ServiceProxy("/turtle1/set_pen",Ps4Data,callback,queue_size = 1)# hint: the srv type is SetPen
    # fill in the other service client object...
    
    rospy.spin()
