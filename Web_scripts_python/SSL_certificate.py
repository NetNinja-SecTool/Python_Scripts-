import ssl
import socket
def certificateInformation():
    # Taking URL input from the user
    url = input("Enter the domain to get SSL certificate information: ")
    while not url:
        url = input("Please enter a valid domain: ")

    try:
        context = ssl.create_default_context()
        server = context.wrap_socket(socket.socket(), server_hostname=url)
        server.connect((url, 443))
        certificate = server.getpeercert()

        print("[+]Certificate Serial Number:", certificate.get('serialNumber'))
        print("[+]Certificate SSL Version:", certificate.get('version'))
        print("[+]Certificate:", certificate)

    except Exception as e:
        print(f"Error: {e}")
        print("Please check the domain and try again.")

# Call the function
certificateInformation()
