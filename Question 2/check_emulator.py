"""
Check if an Android emulator is running using adb.
"""
import subprocess


def is_emulator_running():
    try:
        # Run adb devices command
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")
        # Skip the first line (header)
        devices = [line for line in lines[1:] if line.strip()]
        # Look for emulator in the device list
        for device in devices:
            if device.startswith("emulator-") and "device" in device:
                return True
        return False
    except Exception as e:
        print(f"Error checking emulator: {e}")
        return False


if __name__ == "__main__":
    if is_emulator_running():
        print("Android emulator is running.")
    else:
        print("No Android emulator detected.")
