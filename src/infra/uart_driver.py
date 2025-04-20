import serial
import time
from typing import Dict, Optional


class UartDriver:
    def __init__(
        self,
        port: str,
        baudrate: int,
        drawer_id_serial_command_map: Dict[int, str]
    ):
        self.port = port
        self.baudrate = baudrate
        self.serial: Optional[serial.Serial] = None
        self.drawer_id_serial_command_map = drawer_id_serial_command_map

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

        if drawer_id not in self.drawer_id_serial_command_map:
            raise ValueError(f"No serial command defined for drawer_id: {drawer_id}")

        command = f"{self.drawer_id_serial_command_map[drawer_id]}\r\n"
        self.serial.write(command.encode("utf-8"))
        self.serial.flush()
