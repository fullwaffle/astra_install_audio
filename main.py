import subprocess


def get_product_name():
    command = f"dmidecode -t baseboard | grep -i 'Product Name' | sed 's/\tProduct Name: //' | tr -d '\n'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    return result


def install_package(package_name):
    subprocess.run(["apt-get", "update", "-y"])
    command = ["apt-get", "install", "-y", package_name]
    subprocess.run(command)


def delete_package(package_name):
    subprocess.run(["apt-get", "remove", "-y", package_name])
    subprocess.run(["apt-get", "autoremove", "-y"])


if __name__ == "__main__":
    product_name = get_product_name()
    if product_name.stdout == "NS685Is4":
        install_package("bsp-ns685-astra")
    else:
        delete_package("bsp-ns685-astra")
