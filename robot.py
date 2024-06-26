# importing modules
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.tools import wait
from pybricks.tools import hub_menu


# setup

BLACK = 5
WHITE = 42
TARGET = 23

hub = PrimeHub()
wheel_right = Motor(Port.C, Direction.COUNTERCLOCKWISE)
wheel_left = Motor(Port.D)
arm_left = Motor(Port.E)
arm_right = Motor(Port.B)
sensor_left = ColorSensor(Port.F)
sensor_right = ColorSensor(Port.A)
chassis = DriveBase(wheel_left, wheel_right, 62.4, 135)
chassis.use_gyro(True)
hub.imu.reset_heading(0)
chassis.settings(straight_speed=250)
chassis.settings(turn_rate=100)

# vars
colors = (
    Color.BLACK,
    Color.RED,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.WHITE,
    Color.NONE,
)
sensor_left.detectable_colors(colors)
sensor_right.detectable_colors(colors)


# functions
# def to_angle(angle, speed):
#     start_angle = hub.imu.heading()
#     math = angle - start_angle
#     chassis.settings(turn_acceleration=speed)
#     if math < 180 and math > 0:
#         chassis.turn(start_angle + angle)``
#     if math > -180 and math < 0:
#         chassis.turn(start_angle - angle)
#     if math > 180 and math > 0:
#         chassis.turn(start_angle - angle)
#     if math < -180 and math < 0:
#         chassis.turn(start_angle + angle)


def turn_to(angle):
    print(hub.imu.heading())
    start_angle = (hub.imu.heading() + 360) % 360  # 208
    print(start_angle)
    deg_to_turn = (angle - start_angle) % 360  # 242
    print(deg_to_turn)

    if deg_to_turn >= 180:
        chassis.turn(deg_to_turn - 360)
    else:
        chassis.turn(deg_to_turn)


def turn_to_right(angle):
    start_angle = hub.imu.heading() % 360  # 208
    deg_to_turn = angle - start_angle % 360  # 242
    chassis.turn(deg_to_turn)


def rightround(thing):
    chassis.straight(thing)
    thing = thing * -1
    chassis.straight(thing / 2)


def duck():
    arm_left.run_time(1000, 500)


def till_black(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_left.reflection() > 9:
        print(sensor_left.color())
        pass

    chassis.stop()


def till_black_right(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_right.reflection() > 9:
        print(sensor_right.color())
        pass


def till_white(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_right.color() != Color.WHITE:
        print(sensor_right.color())
        pass

    chassis.stop()


def till_not_black(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_right.color() == Color.BLACK:
        pass

    chassis.stop()


def s_icon():
    hub.display.icon(
        [
            [0, 100, 100, 100, 100],
            [100, 0, 0, 0, 0],
            [0, 100, 100, 100, 0],
            [0, 0, 0, 0, 100],
            [0, 100, 100, 100, 0],
        ]
    )


def t_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 100],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
        ]
    )


def a_icon():
    hub.display.icon(
        [
            [0, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
        ]
    )


def r_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
        ]
    )


def b_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 0],
        ]
    )


def l_icon():
    hub.display.icon(
        [
            [100, 0, 0, 0, 0],
            [100, 0, 0, 0, 0],
            [100, 0, 0, 0, 0],
            [100, 0, 0, 0, 0],
            [100, 100, 100, 100, 0],
        ]
    )


def i_icon():
    hub.display.icon(
        [
            [0, 100, 100, 100, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 100, 100, 100, 0],
        ]
    )


def z_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 100],
            [0, 0, 0, 100, 0],
            [0, 0, 100, 0, 0],
            [0, 100, 0, 0, 0],
            [100, 100, 100, 100, 100],
        ]
    )


def follow_line(speed: int, seconds: float, sensor: ColorSensor, side="right", kp=1.5):
    error = sensor.reflection() - TARGET
    timer = StopWatch()
    timer.reset()
    direction = 1 if speed > 0 else -1
    if side == "right":
        direction = direction * -1
    while timer.time() < seconds * 1000:
        error = sensor.reflection() - TARGET
        change = int(error * kp * direction)
        wheel_right.dc(speed + change)
        wheel_left.dc(speed - change)


def follow_line_until_black(
    speed: int, sensor: ColorSensor, detection_sensor: ColorSensor, side="right", kp=1.5
):
    error = sensor.reflection() - TARGET
    direction = 1 if speed > 0 else -1
    if side == "right":
        direction = direction * -1
    while detection_sensor.reflection() > 9:
        error = sensor.reflection() - TARGET
        change = int(error * kp * direction)
        wheel_right.dc(speed + change)
        wheel_left.dc(speed - change)


def clean_wheels():
    chassis.drive(720, 0)
    while "1 + 1 = 3":
        pass
def run_1():
    chassis.straight(200)
    arm_right.run_angle(700, 360)

def stats():
    precent = hub.battery.current() / 2100 * 100
    print("battery: ", hub.battery.current(), "mAh")
    print("battery: ", precent, "%")
    # wheel_left.run_time(300, 1500)


selected = hub_menu("1", "2", "3", "4", "5", "6", "7", 99, "9")


if selected == "1":
    run_1()
elif selected == "2":
    run_2()
elif selected == "3":
    run_3()
elif selected == "4":
    run_4()
elif selected == "5":
    run_5()
elif selected == "6":
    run_6()
elif selected == "7":
    run_7()
elif selected == 99:
    stats()
elif selected == "9":
    clean_wheels()

s_icon()
wait(400)
t_icon()
wait(400)
a_icon()
wait(400)
r_icon()
wait(400)
b_icon()
wait(400)
l_icon()
wait(400)
i_icon()
wait(400)
t_icon()
wait(400)
z_icon()
wait(400)
