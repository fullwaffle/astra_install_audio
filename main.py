import subprocess

LAPTOP_MOTHERBOARD: str = "NS685Is4"
AUDIO_PACKAGE: str = "bsp-ns685-astra"


def get_product_name() -> str:
    """
    Функция для получения имени baseboard

    :return: Возвращает имя baseboard
    """
    command = f"dmidecode -t baseboard | grep -i 'Product Name' | sed 's/\tProduct Name: //' | tr -d '\n'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    return result.stdout


def install_package(package_name: str) -> None:
    """
    Функция обновляет репозитории и устанавливает пакет

    :param package_name: Пакет для установки звука на NS685Is4
    :return: None
    """
    subprocess.run(["apt-get", "update"])
    command = ["apt-get", "install", "-y", package_name]
    subprocess.run(command)


def delete_package(package_name: str) -> None:
    """
    Функция удаляет пакет и его зависимости

    :param package_name: Пакет для установки звука на NS685Is4
    :return: None
    """
    subprocess.run(["apt-get", "remove", "-y", package_name])
    subprocess.run(["apt-get", "autoremove", "-y"])


if __name__ == "__main__":
    product_name: str = get_product_name()
    if product_name == LAPTOP_MOTHERBOARD:
        install_package(AUDIO_PACKAGE)  # Установка звука на Astra Linux 1.7.4 для NS685Is4 ноута
    else:
        delete_package(AUDIO_PACKAGE)
