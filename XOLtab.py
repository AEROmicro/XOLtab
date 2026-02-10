#!/usr/bin/env python3

import platform
import psutil
import shutil
import datetime
import subprocess
import getpass
import os
import sys

# Developed by AEROforge
# Supervised and Founded by AEROxol
# Programming and Debugging by AEROxol

# Offical Github Repository
# https://github.com/AEROmicro/XOLtab

# Offical Website
# https://sites.google.com/view/aeroforge/

# Licensed under GNU General Public License v3.0 (GPLv3)
# Anyone redistributing or modifying this code must retain this notice.

# Copyright (C) 2026 ÆROforge (AEROxol)
# Licensed under GNU GPLv3
# Trademark: XOLtab is a brand of ÆROforge

try:
    import GPUtil
except ImportError:
    GPUtil = None

# ANSI escape sequences for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33}"

def get_cpu_model():
    try:
        output = subprocess.check_output(['lscpu'], universal_newlines=True)
        for line in output.splitlines():
            if 'Model name' in line:
                return line.split(':')[1].strip()
    except Exception:
        pass
    return platform.processor()

def get_graphics_info():
    gpus = []
    if GPUtil:
        gpus = GPUtil.getGPUs()
    graphics_names = [gpu.name for gpu in gpus]
    if graphics_names:
        return ", ".join(graphics_names)
    else:
        try:
            lspci_output = subprocess.check_output(['lspci'], universal_newlines=True)
            for line in lspci_output.splitlines():
                if 'VGA' in line or '3D' in line:
                    parts = line.split(':')
                    if len(parts) > 2:
                        return parts[2].strip()
        except Exception:
            pass
        return "No graphics info available"

def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        secs_left = battery.secsleft
        capacity = battery.max_capacity if hasattr(battery, 'max_capacity') else 'N/A'  # Might not be available
        return percent, capacity
    return None, None

def get_desktop_env():
    import os
    return os.environ.get('XDG_CURRENT_DESKTOP') or 'Unknown'

def get_distro_name():
    path = "/etc/os-release"
    if os.path.isfile(path):
        try:
            with open(path, 'r') as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        # Remove 'PRETTY_NAME=' and quotes
                        return line.strip().split("=",1)[1].strip().strip('"')
        except Exception as e:
            print(f"Error reading {path}: {e}")
    return "Linux"

def get_device_model():
    os_type = platform.system()
    if os_type == "Linux":
        try:
            output = subprocess.check_output(['dmidecode', '-s', 'system-product-name'], universal_newlines=True)
            return output.strip()
        except:
            return "Unknown"
    elif os_type == "Darwin":
        try:
            output = subprocess.check_output(['sysctl', '-n', 'hw.model'], universal_newlines=True)
            return output.strip()
        except:
            return "Unknown"
    elif os_type == "Windows":
        try:
            output = subprocess.check_output(
                ['powershell', '-Command',
                 "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -ExpandProperty Model"],
                universal_newlines=True)
            return output.strip()
        except:
            return "Unknown"
    else:
        return "Unknown"


def get_system_info():
    hostname = platform.node()

    # OS and Kernel
    os_name = platform.system()
    if os_name == "Linux":
        os_name = get_distro_name()
    kernel_version = platform.release()

    # CPU
    cpu_model = get_cpu_model()
    cpu_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()

    # Memory
    mem = psutil.virtual_memory()

    # Swap
    swap = psutil.swap_memory()

    # Disk
    disk = psutil.disk_usage('/')

    # Uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = (datetime.datetime.now() - boot_time).total_seconds()
    uptime_str = str(datetime.timedelta(seconds=int(uptime_seconds)))

    # Graphics
    graphics_info = get_graphics_info()

    # Battery
    batt_percent, batt_capacity = get_battery_info()

    # User
    user_name = getpass.getuser()

    # DE and WM
    de = get_desktop_env()

    # Device model
    device_model = get_device_model()

    # Shell
    shell = shutil.which('bash') or shutil.which('zsh') or 'N/A'

    return {
        "Host": hostname,
        "User": user_name,
        "OS": os_name,
        "Kernel Version": kernel_version,
        "Uptime": uptime_str,
        "Desktop Environment": de,
        'Device Model': device_model,
        "CPU": f"{cpu_model} ({cpu_count} cores, {cpu_freq.current:.1f} MHz)" if cpu_freq else cpu_model,
        "Memory": f"{mem.total / (1024**3):.2f} GB",
        "Memory Used": f"{mem.used / (1024**3):.2f} GB",
        "Memory Usage": f"{mem.percent}%",
        "Swap Used": f"{swap.used / (1024**3):.2f} GB",
        "Swap Total": f"{swap.total / (1024**3):.2f} GB",
        "Swap Usage": f"{swap.percent}%",
        "Disk": f"{disk.percent}% used of {disk.total / (1024**3):.2f} GB",
        "Graphics": graphics_info,
        "Battery": f"{batt_percent}%" if batt_percent is not None else "N/A",
        "Shell": shell,
    }

def print_bold(title):
    print(f"{BOLD}{title}{RESET}")

def display_info():
    info = get_system_info()
    print(f"\n{BOLD}XOLtab - System Information{RESET}")
    print("---------------------------")
    for key, value in info.items():
        print_bold(f"{CYAN}{key}:{RESET} {value}")

if __name__ == "__main__":
    display_info()
