from robot_control_class import RobotControl
import time

rc = RobotControl(robot_name="summit")

rc.move_straight_time("forward", 0.3, 5)
rc.turn("counter-clockwise", 0.3, 7.98)

rc.move_straight_time("forward", 0.3, 7.5)
rc.turn("counter-clockwise", 0.3, 8.5)
rc.move_straight_time("forward", 0.3, 7)