import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, wait

from device_list import devices
from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
    SSHException,
)

timestamp_format = "%Y-%m-%d_%H:%M:%S"
config_type = "running"


def get_config(device):
    current_time = datetime.now().strftime(timestamp_format)
    try:
        with ConnectHandler(**device) as net_connect:
            print(f"Getting config for {device['host']}...")
            net_connect.enable()
            running_config = net_connect.send_command(
                f"show {config_type}-config"
            )
            with open(f"{device['host']}_{current_time}.txt", "w") as f:
                f.writelines(running_config)
    except (
        ValueError,
        SSHException,
        NetMikoAuthenticationException,
        NetMikoTimeoutException,
    ):
        print(f"{device['host']} : {sys.exc_info()[1]}")


if __name__ == "__main__":
    max_threads = 5
    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for one_device in devices:
        future = pool.submit(get_config, one_device)
        future_list.append(future)

    wait(future_list)
