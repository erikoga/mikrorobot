# gets euler angles from a topic and converts to quaternions and publish to a new topic
# # see tf at roswiki
#  publish using datatype quaternions
#  input:	gx,y,z - gimbal xyz ( roll, pitch, yaw)
#  			ax,y,z - an
#  			mx,y,z -
#  			???

# trenger en listener, en databehandler og en publish del.

import rospy
