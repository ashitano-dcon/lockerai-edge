from collections.abc import Callable
from typing import Any

from pynput.keyboard import Listener


class QrCodeReaderDriver:
    def __init__(self, callback: Callable[[str], None], cleanup: Callable[[], None] | None = None) -> None:
        self.__callback = callback
        self.__cleanup = cleanup
        self.__data: list[str] = []

    def start(self) -> None:
        print("Start driving QR Code Reader.")
        with Listener(on_press=self.__on_press) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                listener.stop()
                print("Stop driving QR Code Reader.")
                if self.__cleanup:
                    self.__cleanup()

    def __on_press(self, key: Any) -> None:
        print(f"on_press key: {key}")
        if str(key) != "Key.enter":
            try:
                self.__data.append(key.char[0:1])
            except AttributeError:
                return
        else:
            qr_code = "".join(self.__data)
            self.__callback(qr_code)
