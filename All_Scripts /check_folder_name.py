import os

def get_folder_names_in_drive(drive_letter):
    drive_path = f"{drive_letter}:\\"

    try:
        folder_names = [item for item in os.listdir(drive_path) if os.path.isdir(os.path.join(drive_path, item))]
        return folder_names

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    drive_letter = input("Enter the drive letter (e.g., C): ").upper()

    if len(drive_letter) == 1 and "A" <= drive_letter <= "Z":
        folder_names = get_folder_names_in_drive(drive_letter)

        if isinstance(folder_names, list):
            print(f"Folder names in drive {drive_letter}:")
            for folder_name in folder_names:
                print(f"- {folder_name}")
        else:
            print(folder_names)
    else:
        print("Invalid drive letter. Please enter a single uppercase letter (e.g., C).")
