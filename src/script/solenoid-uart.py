import os
from dotenv import load_dotenv

from infra.uart_driver import UartDriver

load_dotenv()

uart_driver = UartDriver(
    port=str(os.environ.get("UART_PORT", "/dev/serial0")),
    baudrate=int(os.environ.get("UART_BAUDRATE", 9600)),
    drawer_id_serial_command_map={
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5"
    }
)


if __name__ == "__main__":
    uart_driver.setup()

    uart_driver.open_drawer(1)
    uart_driver.open_drawer(2)
    uart_driver.open_drawer(3)
    uart_driver.open_drawer(4)
    uart_driver.open_drawer(5)

    uart_driver.cleanup()
