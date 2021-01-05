#!/usr/bin/env python3
#SPDX-License-Identifier: GPL-3.0
#
# Copyright (C) 2020 KaitoToda + RyuichiUeda.  All rights reserved.
#

import rospy
import random
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up',Int32,queue_size=1)
rate = rospy.Rate(20)
n = 1
while not rospy.is_shutdown():
    n = random.randint(0,100)
    pub.publish(n)
    rate.sleep()
