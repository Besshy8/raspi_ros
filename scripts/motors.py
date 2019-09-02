#!/usr/bin/env python
#encoding: utf8
import rospy 
from std_srvs.srv import Trigger,TriggerResponse

def srvCallbackOn(srv):    ##srvがないとerror processing request: srvCallback() takes no arguments (1 given)
    print("----------------------")
    print("Called srvCallbackOn() func")
    res = TriggerResponse()
    with open("/dev/rtmotoren0","w") as w:
        w.write("1\n")  ##1でも可
    res.success = True
    res.message = "motor_on"
    return res    ##returnでTriggerresponseを返さないとservice cannot process request: service handler returned None

def srvCallbackOff(srv):
    print("----------------------")
    print("Called srvCallbackOff() func")
    res = TriggerResponse()
    with open("/dev/rtmotoren0","w") as w:
        w.write("0\n")  ##1でも可
    res.success = True
    res.message = "motor_off"
    return res

if __name__ == "__main__":
    rospy.init_node("Motors")
    srvs_on = rospy.Service("motor_on",Trigger,srvCallbackOn)
    srv_off = rospy.Service("motor_off",Trigger,srvCallbackOff)   ##srv_offが無くても動く
    rospy.spin()