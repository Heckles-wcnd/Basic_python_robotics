from robot_control_class import RobotControl

rc = RobotControl()

list = rc.get_laser_full()

print(list[0])
print(list[360])
print(list[719])