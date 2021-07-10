import rospy 
import random 
from geometry.msgs import Twist 
from nav_msgs.msgs import LaserScan 

def sample_array(length) :
    sample =[]
    for i in range(length) : 
        sample.append(random.randint(0,1)) 
    print ("Returning sample array of length {} : {}".format(length, sample))
    return sample 


#sample_array()
