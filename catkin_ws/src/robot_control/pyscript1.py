from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(320)

print ("The distance measured is: ", a, " m.")