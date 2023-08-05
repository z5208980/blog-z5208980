---
title: "ROS Topics"
date: "2020-09-30"
tags: ["ROS", "Robotics"]
image: ""
gradients: ["#FAD961", "#F76B1C"]
---

## RosTopic
most important concept in ROS. We can think of a topic as a pipe that can write and read.

publishing a topic (used to communicate with the robot) `rostopic pub /cmd_vel geometry_msgs/Twist “linear: …"` you should tab to get all the arguments for the topic.

`rostopic list` `rostopic info /topic` get information (like doc such as type, publishers, and subscribers) `rostopic echo /topic` read information of a topic

### Messages
This is basically **type** rosmsg show `std_msgs/Int32` this message (type) will have an variable called `data` which is message (type) `int32`.

### ROS services
they have server (service) and client (calls the service) `roslaunch service service.launch`
`
client calling (in new terminal) This will call `rosservice call /service args`

### ROS actions (similarly to ROS service)
Difference is that ROS service we can perform one one action at a time. Actions allows us to get feedback and perform actions

### Debugging (using Rviz)
`rosin vis rviz`

`roslaunch <pkg_name> <launch_file> pkg_name`

- launch
- msg
- src
- CMakeList.txt
- package.xml
To navigate to ROS package use `rocd <pkg_name>`

In `msg` dir, you can create custom message, given in `.msg`,

`Date.msg`. **Note**: This is a file

```
float32 years
float32 month
float32 day
```

then in `CMakeList.txt`
```c
add_message_files(
Date.msg
)
```

**Note**: This is not the entire steps, as there is stuff like `message_runtime` and `message_generation` but I don’t very understand that stuff so I won’t add.

To check the message, 
`rosmsg show Date`

launch_file
```xml
<launch>
	<node pkg type name output> </node>
</launch>
```

### catkin_ws
This is where all the ROS packages will be installed.

To create a package, we need to be in the `catkin_ws/src`
To init boilerplate of ROS package use cmd, `catkin_create_pkg pkg_name rospy`
To compile the package, 
`cd ~/catkin_ws` 
`catkin_make`

## ROS Publisher in python
```py
#! /usr/bin/env_python

import rospy
from std_msgs.msg import Int32	# impoty Int32 message (type) from the std_msgs package
# from geometry_msgs.msg import Twist

rospy.init_node(‘topic_publisher’) 	# To init a RosNode

# Publisher(topic, type)
pub = rospy.Publisher('counter', Int32)# Create a publisher object

rate = rospy.Rate(2)		# Explain later

count = Int32		# init var of type Int32
count.data = 0
# For Twist
# twist = Twist()
# twist.linear.x = 0.5
# twist.angular.z = 0.5

while not rospy.is_shutdown():		# not Ctrl C
	pub.pushlish(count)		# publishing the msg, so when someone read /counter (given by pub var)
	count.data += 1
	rate.sleep()
```

## Ros Subscriber in python
```py
#! /usr/bin/env_python

import rospy
from std_msgs.msg import Int32	# impoty Int32

def callback(msg):
	print(msg.data)

rospy.init_node('topic_subscriber')
# Whenever /counter is published using `rostopic pub`, 
# then callback func will be called.
sub = rospy.Subscriber('/counter', Int32, callback)	
rospy.spin()
```

### ROS Node
ROS Nodes is a process that execute a ROS program. We need to launch it by launching a ROS Node `rosnode list` allows you to check all node running `rosnode kill /node` end ROS Node

### ROS Param
`rosparam list`

### Roscore
`roscore`

### Env variable
`export | grep ROS`