from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor,ColorSensor,UltrasonicSensor
from ev3dev2.led import Leds


class EV3DEV_Body:

    __ts = TouchSensor()
    __ultrasonic_sensor = UltrasonicSensor()
    __colorSensor = ColorSensor()
    __leds = Leds()

    def __init__(self):
        pass

    def _motor_move(self,motor):
        pass

    def _motors_move(self,time):
        pass
    
    def get_bumper(self):
        return self.__ts.is_pressed
    
    def get_color(self):   
        return self.__colorSensor.MODE_COL_COLOR
    
    def set_led_color(self , color : str, led : str ):
        self.__leds.set_color(led, color)
               
    def get_ultrasonic_sensors(self):     
            self.__ultrasonic_sensor().MODE_US_SI_CM