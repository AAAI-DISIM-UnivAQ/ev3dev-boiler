from EV3DEV_Body import EV3DEV_Body
class EV3DEV_Controller:
    
    
    def __init__(self):
        self.__body = EV3DEV_Body()


    def change_led_color(self,sensor : str ,color : str):
        if sensor == 'ultrasonic':
            if self.__body.get_ultrasonic_sensors() <= 3 :
                self.__body.set_led_color(color)
                print(color)
        if sensor == 'bumper':         
            self.__body.set_led_color(color)
            print(color)