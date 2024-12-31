from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(360)

if a < 1:
    rc.stop_robot()
    print("The distance is ", a)
else: 
    rc.move_straight()
    print("The distance is ", a)