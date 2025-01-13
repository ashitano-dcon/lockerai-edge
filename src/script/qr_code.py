from infra.qr_code_reader_driver import QrCodeReaderDriver


def callback(qr_code: str) -> None:
    print(f"callback qr_code:{qr_code}")


qr = QrCodeReaderDriver(callback)
qr.start()
