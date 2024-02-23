import os
import imghdr
def count_files_by_type(directory):
    folder_count = 0
    text_file_count = 0
    video_count = 0
    image_count = 0
    xml_file_count = 0
    zip_file_count = 0
    rar_file_count = 0
    doc_file_count = 0
    pdf_file_count = 0

    for root, dirs, files in os.walk(directory):
        folder_count += len(dirs)

        for file in files:
            file_path = os.path.join(root, file)

            if file.lower().endswith(('.txt', '.doc', '.docx', '.pdf')):
                text_file_count += 1
                if file.lower().endswith('.doc'):
                    doc_file_count += 1
                elif file.lower().endswith('.pdf'):
                    pdf_file_count += 1
            elif is_video_file(file_path):
                video_count += 1
            elif is_image_file(file_path):
                image_count += 1
            elif file.lower().endswith('.xml'):
                xml_file_count += 1
            elif file.lower().endswith('.zip'):
                zip_file_count += 1
            elif file.lower().endswith('.rar'):
                rar_file_count += 1

    print("Counts:")
    print(f"Number of Folders: {folder_count}")
    print(f"Number of Text Files: {text_file_count}")
    print(f"Number of Video Files: {video_count}")
    print(f"Number of Image Files: {image_count}")
    print(f"Number of XML Files: {xml_file_count}")
    print(f"Number of ZIP Files: {zip_file_count}")
    print(f"Number of RAR Files: {rar_file_count}")
    print(f"Number of DOC Files: {doc_file_count}")
    print(f"Number of PDF Files: {pdf_file_count}")

    return folder_count, text_file_count, video_count, image_count, xml_file_count, zip_file_count, rar_file_count, doc_file_count, pdf_file_count

def is_video_file(file_path):
    # Add more video file extensions as needed
    video_extensions = ('.mp4', '.avi', '.mkv')
    return file_path.lower().endswith(video_extensions)

def is_image_file(file_path):
    # Use imghdr to check if the file is an image
    return imghdr.what(file_path) is not None

def is_usb_connected(usb_directory):
    return os.path.exists(usb_directory)

def main():
    usb_directory = 'I:\\'  # Change this to the path of your USB drive

    if not is_usb_connected(usb_directory):
        print("No USB connected.")
        return

    count_files_by_type(usb_directory)

if __name__ == "__main__":
    main()
