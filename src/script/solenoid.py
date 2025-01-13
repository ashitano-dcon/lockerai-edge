from dotenv import load_dotenv

from infra.gpio_driver import GpioDriver

load_dotenv()

gpio_driver = GpioDriver(
    drawer_id_pin_map={
        1: 23,
        2: 24,
    }
)


if __name__ == "__main__":
    gpio_driver.setup()

    gpio_driver.open_drawer(2)

    gpio_driver.cleanup()
