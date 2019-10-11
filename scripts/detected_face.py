#!/usr/bin/env python
#encoding: utf8
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import math
from geometry_msgs.msg import Twist 

def callback(msg):
    ##print("recieve image")
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    ##print(type(cv_image))
    print(cv_image.shape)
    print(cv_image.shape[1])

    cascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(cv_image,cv2.COLOR_RGB2GRAY)
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    for (x, y, w, h) in face:
        img_det = cv2.rectangle(cv_image, (x,y),(x + w , x + h) , (0,255,0) , 3)
    
    ##show_img_det = cv2.cvtColor(img_det, cv2.COLOR_BGR2RGB)
    ##print(type(show_img_det))

    c = cv_image.shape[1] / 2
    d = c - (x + w/2)
    print(c)
    print(d)

    d_std = d / 320
    p = d_std * (math.pi / 2)

    """
    m = Twist()
    m.angular.z = p
    pub_cmdvel.publish(m)

    """

    try:
        pub.publish(bridge.cv2_to_imgmsg(img_det,"bgr8"))
    except CvBridgeError as e:
        print(e)

if __name__ == "__main__":
    rospy.init_node("RectangleFace")
    sub = rospy.Subscriber("cv_camera/image_raw",Image, callback)
    pub = rospy.Publisher("image",Image,queue_size=10)
    pub_cmdvel = rospy.Publisher("motorCmdvel",Twist,queue_size=10)
    rospy.spin()