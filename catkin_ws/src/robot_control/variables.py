from robot_control_class import RobotControl
rc = RobotControl()

laser1 = rc.get_laser(619)
laser2 = rc.get_laser(210)

print("I get ", laser1, laser2)