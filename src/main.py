import os

from dotenv import load_dotenv

from infra.gpio_driver import GpioDriver
from infra.qr_code_reader_driver import QrCodeReaderDriver
from service import ApiClient

load_dotenv()

client = ApiClient(base_url=str(os.environ.get("API_BASE_URL")))

drawer_id_pin_map = {
    1: 23,
    2: 24,
}
gpio_driver = GpioDriver(
    drawer_id_pin_map,
)


def main(user_id: str) -> None:
    user = client.find_user(user_id)
    if user is None:
        client.update_locker_status(
            locker_id=str(os.environ.get("LOCKER_ID")),
            type="ERROR",
            name="認証エラー",
            description="認証に失敗しました。QRコードが正しいかご確認ください。",
        )
        return
    print(f"Found user. user_id: {user.id}")
    client.update_locker_status(
        locker_id=str(os.environ.get("LOCKER_ID")),
        type="SUCCESS",
        name="認証成功",
        description=f"こんにちは、{'管理者 ' if user.role == 'OCCUPIER' else ''}{user.name}さん。",
    )

    if user.lost_and_found_state == "DELIVERING":
        drawer = client.put_in_lost_item(user.id)
        print(f"Put in lost item. drawer_id: {drawer.id}")
        client.update_locker_status(
            locker_id=str(os.environ.get("LOCKER_ID")),
            type="INFO",
            name="拾得物受付",
            description="自動でロッカーが開きます。拾得物を収納し、手動でロッカーを閉めてください。",
        )
        gpio_driver.open_drawer(drawer.id)
    elif user.lost_and_found_state == "RETRIEVING":
        drawer = client.take_out_lost_item(user.id)
        print(f"Take out lost item. drawer_id: {drawer.id}")
        client.update_locker_status(
            locker_id=str(os.environ.get("LOCKER_ID")),
            type="INFO",
            name="遺失物受付",
            description="自動でロッカーが開きます。遺失物を取り出し、手動でロッカーを閉めてください。",
        )
        gpio_driver.open_drawer(drawer.id)
    elif user.role == "OCCUPIER":
        for drawer_id in drawer_id_pin_map:
            gpio_driver.open_drawer(drawer_id)
    else:
        print("Found user, but lost_and_found_state is NONE.")
        client.update_locker_status(
            locker_id=str(os.environ.get("LOCKER_ID")),
            type="WARN",
            name="ステータスエラー",
            description="ユーザーのステータスが不正です。管理者にお問い合わせください。",
        )


if __name__ == "__main__":
    gpio_driver.setup()

    qr_code_reader_driver = QrCodeReaderDriver(
        lambda qr_code: main(qr_code.replace("−", "-").strip()),  # noqa: RUF001
        gpio_driver.cleanup,
    )
    qr_code_reader_driver.start()
