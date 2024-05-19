from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub()


wheel_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
wheel_right = Motor(Port.D)
arm_left = Motor(Port.E)
arm_right = Motor(Port.A)
Sensor_right = ColorSensor(Port.F)
chassis = DriveBase(wheel_left, wheel_right,62.4, 80)
chassis.use_gyro(True)
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


