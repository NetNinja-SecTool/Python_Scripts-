import winreg

def get_installed_applications():
    try:
        key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key_handle = winreg.OpenKey(reg, key)

        installed_applications = []

        for i in range(winreg.QueryInfoKey(key_handle)[0]):
            subkey_name = winreg.EnumKey(key_handle, i)
            subkey_path = f"{key}\\{subkey_name}"

            try:
                subkey = winreg.OpenKey(reg, subkey_path)
                display_name, _ = winreg.QueryValueEx(subkey, "DisplayName")
                installed_applications.append(display_name)
            except Exception as e:
                pass

        winreg.CloseKey(reg)
        return installed_applications

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    installed_apps = get_installed_applications()

    if isinstance(installed_apps, list):
        print("Installed Applications:")
        for app in installed_apps:
            print(f"- {app}")
    else:
        print(installed_apps)
