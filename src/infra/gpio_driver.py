import time

from RPi import GPIO


class GpioDriver:
    def __init__(self, drawer_id_pin_map: dict[int, int]) -> None:
        self.drawer_id_pin_map = drawer_id_pin_map

    def setup(self) -> None:
        GPIO.setmode(GPIO.BCM)
        for pin in self.drawer_id_pin_map.values():
            GPIO.setup(pin, GPIO.OUT)

    def cleanup(self) -> None:
        GPIO.cleanup()

    def open_drawer(self, drawer_id: int) -> None:
        GPIO.output(self.drawer_id_pin_map[drawer_id], GPIO.HIGH)
        time.sleep(3)
        GPIO.output(self.drawer_id_pin_map[drawer_id], GPIO.LOW)
        time.sleep(3)
