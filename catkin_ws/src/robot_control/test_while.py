from robot_control_class import RobotControl
import time

rc = RobotControl()

update_interval = 0.1  # 每隔 0.1 秒刷新一次
last_update_time = time.time()
dist = rc.get_laser(360)

while dist > 1:
    if time.time() - last_update_time > update_interval:
        dist = rc.get_laser(360)
        last_update_time = time.time()
    rc.move_straight()
    print("Current distance is %.5f" % dist)

rc.stop_robot()
print("Wall is at %.5f" % dist)