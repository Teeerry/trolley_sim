#!/usr/bin/env python  
#coding=utf-8 
import rospy
import tf
from sensor_msgs.msg import Joy

def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.axes[4], msg.axes[3], 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.axes[0]),
                     rospy.Time.now(),
                     "odom",#固定坐标叫什么都可以
                     "base_link")#你的物体的参考系 link标签里面的name属性值都可以

if __name__ == '__main__':
    rospy.init_node('my_tf')
    rospy.Subscriber('joy',
                     Joy,#手柄节点的消息类型
                     handle_turtle_pose)
    rospy.spin()
