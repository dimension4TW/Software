#!/usr/bin/env python
import rospy
import numpy as np
from duckietown_msgs.msg import BoolStamped, Twist2DStamped
from std_msgs.msg import Float32, Int32

class arduinoWheel(object):
    def __init__(self):
        # =========== publisher ===========
        # publish to topic "car_cmd" (you may have to see the code last week)
        self.pub_car_cmd = rospy.Publisher("~car_cmd", Twist2DStamped, queue_size=1)

        # =========== subscriber ===========
        # subscribe to topic "result" (you should see arduino_node.py)
        self.sub_result = rospy.Subscriber("~result", BoolStamped, self.cbresult, queue_size=1)

   # =========== subscribe distance from arduino ===========
    def cbresult(self, msg): 
        print msg
        cmd = Twist2DStamped()
        if msg.data == False:
            print "go forward"
            cmd.v = 0.2
            cmd.omega = 0
            self.pub_car_cmd.publish(cmd)
        else:
            print "go backward"
            cmd.v = -0.2
            cmd.omega = 0
            self.pub_car_cmd.publish(cmd)
if __name__ == "__main__":
    rospy.init_node("arduino_wheel", anonymous = False)
    arduino_node = arduinoWheel()
    rospy.spin()
