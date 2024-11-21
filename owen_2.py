import time
import gopigo3
from search import find
import easygopigo3 as easy
easy_gpg = easy.EasyGoPiGo3()
servo1 = easy_gpg.init_servo("SERVO1")
servo2 = easy_gpg.init_servo("SERVO2")
my_distance_sensor_left = easy_gpg.init_distance_sensor("I2C")
my_distance_sensor_right = easy_gpg.init_distance_sensor("AD2")
GPG = gopigo3.GoPiGo3()
lineFollow = easy_gpg.init_line_follower("AD1")

while True:
    if lineFollow.read("bivariate-str") == "bbwwbb":
        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 50)
    elif lineFollow.read("bivariate-str") == "bwwbbb" or lineFollow.read("bivariate-str") == "wwbbbb" or lineFollow.read("bivariate-str") == "wbbbbb":
        GPG.set_motor_power(GPG.MOTOR_LEFT, -50)
        GPG.set_motor_power(GPG.MOTOR_RIGHT, 50)
    elif lineFollow.read("bivariate-str") == "bbbwwb" or lineFollow.read("bivariate-str") == "bbbbww" or lineFollow.read("bivariate-str") == "bbbbbw":
        GPG.set_motor_power(GPG.MOTOR_LEFT, 50)
        GPG.set_motor_power(GPG.MOTOR_RIGHT, -50)
    else:
        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 0)   
