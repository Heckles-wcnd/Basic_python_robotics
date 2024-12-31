from robot_control_class import RobotControl

rc = RobotControl()

arg = int(input("Input a number:\n"))

laser1 = rc.get_laser(arg)

print("The distance is %.5f" % laser1)