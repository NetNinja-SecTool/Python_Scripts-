import platform
import psutil

def get_system_details():
    try:
        # Platform information
        system_platform = platform.system()
        system_version = platform.version()
        system_architecture = platform.architecture()

        # CPU information
        cpu_info = platform.processor()
        cpu_count = psutil.cpu_count(logical=False)
        logical_cpu_count = psutil.cpu_count(logical=True)

        # Memory information
        memory_info = psutil.virtual_memory()

        # Disk information
        disk_info = psutil.disk_usage('/')

        # Display system details
        print("System Information:")
        print(f"- Platform: {system_platform} {system_version} ({system_architecture[0]} {system_architecture[1]})")
        print(f"- CPU: {cpu_info} ({cpu_count} physical cores, {logical_cpu_count} logical cores)")
        print(f"- Memory: Total: {convert_bytes(memory_info.total)}, Used: {convert_bytes(memory_info.used)}, Free: {convert_bytes(memory_info.available)}")
        print(f"- Disk: Total: {convert_bytes(disk_info.total)}, Used: {convert_bytes(disk_info.used)}, Free: {convert_bytes(disk_info.free)}")

    except Exception as e:
        return f"Error: {e}"

def convert_bytes(bytes):
    # Convert bytes to a human-readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

if __name__ == "__main__":
    system_details = get_system_details()

    if isinstance(system_details, str):
        print(system_details)
