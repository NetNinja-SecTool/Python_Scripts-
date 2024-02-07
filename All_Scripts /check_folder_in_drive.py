import os

def count_folders_in_drive(drive_letter):
    drive_path = f"{drive_letter}:\\"

    try:
        folder_count = sum(1 for item in os.listdir(drive_path) if os.path.isdir(os.path.join(drive_path, item)))
        return folder_count

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    drive_letter = input("Enter the drive letter (e.g., C): ").upper()

    if len(drive_letter) == 1 and "A" <= drive_letter <= "Z":
        folder_count = count_folders_in_drive(drive_letter)

        if isinstance(folder_count, int):
            print(f"Number of folders in drive {drive_letter}: {folder_count}")
        else:
            print(folder_count)
    else:
        print("Invalid drive letter. Please enter a single uppercase letter (e.g., C).")
