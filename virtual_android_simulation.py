import os
import subprocess
import time

def start_emulator(avd_name):
    print(f"Starting Android emulator: {avd_name}")
    emulator_path = r"E:\AnushkaRanjan_PythonInternAssignment\AnushkaR\AppData\Local\Android\Sdk\emulator"  # Update to your emulator path
    try:
        subprocess.Popen([emulator_path, "-avd", avd_name])
        print("Waiting for the emulator to boot...")
        subprocess.run(["adb", "wait-for-device"], check=True)
        print("Emulator is ready!")
    except Exception as e:
        print(f"Failed to start emulator: {str(e)}")

def install_apk(apk_path):
    print(f"Installing APK: {apk_path}")
    try:
        result = subprocess.run(["adb", "install", apk_path], capture_output=True, text=True)
        if result.returncode == 0:
            print("APK installed successfully!")
        else:
            print(f"Failed to install APK: {result.stderr}")
    except Exception as e:
        print(f"Error during APK installation: {str(e)}")

def get_system_info():
    print("Fetching system information...")
    try:
        os_version = subprocess.run(["adb", "shell", "getprop", "ro.build.version.release"], capture_output=True, text=True).stdout.strip()
        device_model = subprocess.run(["adb", "shell", "getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip()
        memory_info = subprocess.run(["adb", "shell", "cat", "/proc/meminfo"], capture_output=True, text=True).stdout
        
        print(f"OS Version: {os_version}")
        print(f"Device Model: {device_model}")
        print("Memory Info:")
        print(memory_info)
    except Exception as e:
        print(f"Error fetching system information: {str(e)}")

if __name__ == "__main__":
    avd_name = "Pixel_4_API_35" 
    apk_path = r"E:\AnushkaRanjan_PythonInternAssignment\AnushkaR\AppData\Local\.android\avd"  # Update to your APK file path

    start_emulator(avd_name)
    time.sleep(5)  
    install_apk(apk_path)
    get_system_info()
