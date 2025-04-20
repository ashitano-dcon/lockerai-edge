import serial
import time
from typing import Dict, Optional


class UartDriver:
    def __init__(self, port: str = "/dev/ttyUSB0", baudrate: int = 9600):
        self.port = port
        self.baudrate = baudrate
        self.serial: Optional[serial.Serial] = None

    def setup(self) -> None:
        self.serial = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=1
        )
        # HACK: Wait for the serial port to be initialized.
        time.sleep(2)

    def cleanup(self) -> None:
        if self.serial and self.serial.is_open:
            self.serial.close()

    def open_drawer(self, drawer_id: int) -> None:
        if not self.serial or not self.serial.is_open:
            raise RuntimeError("UART port is not initialized")

        command = f"{drawer_id}"
        self.serial.write(command.encode())
        self.serial.flush()
