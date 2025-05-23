from collections.abc import Callable
from typing import Any

import keyboard


class QrCodeReaderDriver:
    def __init__(self, callback: Callable[[str], None], cleanup: Callable[[], None] | None = None) -> None:
        self.__callback = callback
        self.__cleanup = cleanup
        self.__data: list[str] = []

    def start(self) -> None:
        print("Start driving QR Code Reader.")
        try:
            keyboard.on_press(self.__on_press)
            keyboard.wait("esc")
        except KeyboardInterrupt:
            print("Stop driving QR Code Reader.")
            if self.__cleanup:
                self.__cleanup()

    def __on_press(self, event: Any) -> None:
        print(f"on_press key: {event.name}")
        if event.name != "enter":
            if len(event.name) == 1:
                self.__data.append(event.name)
        else:
            qr_code = "".join(self.__data)
            self.__callback(qr_code)
            self.__data.clear()
