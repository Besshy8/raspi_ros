#!/usr/bin/env python
#encoding: utf8
import rospy 
from std_srvs.srv import Trigger,TriggerResponse

def srvCallback(srv):    ##srvがないとerror processing request: srvCallback() takes no arguments (1 given)
    print("Called srv_callback func")
    res = TriggerResponse()
    res.success = True
    res.message = "motor_on"
    return res    ##returnでTriggerresponseを返さないとservice cannot process request: service handler returned None

if __name__ == "__main__":
    rospy.init_node("Motors")
    srvs = rospy.Service("motor_on",Trigger,srvCallback)
    rospy.spin()