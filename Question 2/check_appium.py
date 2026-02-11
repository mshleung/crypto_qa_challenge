"""
Check if Appium server is running and responsive.
"""
import requests


def is_appium_running(host="http://localhost", port=4723):
    url = f"{host}:{port}/status"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            status = response.json()
            if status.get("value") or status.get("status") == 0:
                print("Appium server is running and responsive.")
                return True
            else:
                print("Appium server responded but status is not OK.")
                return False
        else:
            print(f"Appium server responded with status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Could not connect to Appium server: {e}")
        return False


if __name__ == "__main__":
    is_appium_running()
