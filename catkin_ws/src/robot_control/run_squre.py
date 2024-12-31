from robot_control_class import RobotControl

class Moverobot:
    def __init__(self, motion, clockwise, speed, time):
        self.rc = RobotControl(robot_name="summit")
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 3.99

    def do_squre(self):
        i = 0
        while(i<4):
            self.move_straight()
            self.turn()
            i+=1
    
    def move_straight(self):
        self.rc.move_straight_time(self.motion, self.speed, self.time)

    def turn(self):
        self.rc.turn(self.clockwise, self.speed, self.time_turn)

rc = RobotControl(robot_name="summit")
rc.move_straight_time("forward", 0.6, 3)

mr1 = Moverobot("forward", "clockwise", 0.6, 2)
mr1.do_squre()

mr2 = Moverobot("forward", "clockwise", 0.6, 4)
mr2.do_squre()
        