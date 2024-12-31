from robot_control_class import RobotControl

rc = RobotControl()

list = rc.get_laser_full()

dict = {'p0':list[0],'p100':list[100],'p200':list[200],'p200':list[200]}

print(dict)