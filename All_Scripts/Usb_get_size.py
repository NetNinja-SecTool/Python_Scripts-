import ctypes
import psutil

def is_external_drive(partition):
    drive_letter = partition.device.split(':')[0]
    drive_type = ctypes.windll.kernel32.GetDriveTypeW(f"{drive_letter}:\\")
    return drive_type == 2  # DRIVE_REMOVABLE

def get_external_usb_drives():
    partitions = psutil.disk_partitions()
    external_drives = []

    for partition in partitions:
        if is_external_drive(partition):
            external_drives.append(partition.device)

    return external_drives

def get_usb_drive_sizes():
    usb_sizes = {}
    external_drives = get_external_usb_drives()

    for drive in external_drives:
        try:
            partition_info = psutil.disk_usage(drive)
            usb_sizes[drive] = partition_info.total
        except PermissionError as e:
            print(f"Error getting information for drive {drive}: {e}")

    return usb_sizes

def main():
    external_drives = get_external_usb_drives()
    usb_sizes = get_usb_drive_sizes()

    if external_drives:
        print("External USB Drives:")
        for drive in external_drives:
            print(drive)

        print("\nUSB Drive Sizes:")
        for drive, size in usb_sizes.items():
            print(f"{drive}: {size / (1024**3):.2f} GB")
    else:
        print("No external USB drives found.")

if __name__ == "__main__":
    main()
