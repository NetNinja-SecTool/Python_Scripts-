import platform
import locale
from datetime import datetime
import os

def get_system_info():
    try:
        # Get country information
        country_info = locale.getdefaultlocale()

        # Get Windows version
        windows_version = platform.version()

        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get username
        username = os.getlogin()

        # Display system information
        print("System Information:")
        print(f"- Country: {country_info[0]}")
        print(f"- Windows Version: {windows_version}")
        print(f"- Date and Time: {current_datetime}")
        print(f"- Username: {username}")

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    system_info = get_system_info()

    if isinstance(system_info, str):
        print(system_info)
