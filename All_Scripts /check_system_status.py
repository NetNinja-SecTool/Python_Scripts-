import psutil
import platform

def check_windows_security():
    system_platform = platform.system()

    if system_platform != "Windows":
        return "This script is intended for Windows systems only."

    try:
        # Check firewall status
        firewall_status = check_firewall_status()

        # Check antivirus status
        antivirus_status = check_antivirus_status()

        # Check Windows Defender status
        defender_status = check_windows_defender_status()

        # Check if automatic updates are enabled
        auto_update_status = check_auto_update_status()

        # Display results
        print("Security Information:")
        print(f"- Firewall Status: {firewall_status}")
        print(f"- Antivirus Status: {antivirus_status}")
        print(f"- Windows Defender Status: {defender_status}")
        print(f"- Automatic Updates Status: {auto_update_status}")

    except Exception as e:
        return f"Error: {e}"


def check_firewall_status():
    firewall = psutil.win_service_get('MpsSvc')
    return "Enabled" if firewall and firewall.status() == 'running' else "Disabled"


def check_antivirus_status():
    # This is a basic check; you may need to adjust it based on your antivirus software
    antivirus_processes = ['McSACore.exe', 'avp.exe', 'avguard.exe', 'avgsvc.exe']

    for process_name in antivirus_processes:
        if any(p.info['name'] == process_name for p in psutil.process_iter(['pid', 'name'])):
            return "Installed and Running"

    return "Not Found or Not Running"


def check_windows_defender_status():
    defender = psutil.win_service_get('WinDefend')
    return "Enabled" if defender and defender.status() == 'running' else "Disabled"


def check_auto_update_status():
    auto_update = psutil.win_service_get('wuauserv')
    return "Enabled" if auto_update and auto_update.status() == 'running' else "Disabled"


if __name__ == "__main__":
    security_info = check_windows_security()

    if isinstance(security_info, str):
        print(security_info)
