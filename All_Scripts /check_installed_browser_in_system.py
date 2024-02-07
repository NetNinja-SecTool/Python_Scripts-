import winreg


def get_installed_browsers():
    try:
        browser_keys = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe",
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\firefox.exe",
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\iexplore.exe",
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\msedge.exe",
            # Add additional browser registry keys as needed
        ]

        installed_browsers = []

        for key_path in browser_keys:
            try:
                reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
                key_handle = winreg.OpenKey(reg, key_path)
                browser_path, _ = winreg.QueryValueEx(key_handle,None)
                installed_browsers.append((key_path.split('\\')[-1], browser_path))
                winreg.CloseKey(reg)
            except FileNotFoundError:
                pass

        return installed_browsers

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    installed_browsers = get_installed_browsers()

    if isinstance(installed_browsers, list):
        print("Installed Browsers:")
        for browser_name, browser_path in installed_browsers:
            print(f"- {browser_name}: {browser_path}")
    else:
        print(installed_browsers)
