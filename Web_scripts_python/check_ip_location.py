import requests

def IP2Location():
    # Taking IP address input from the user
    ip_address = input("Enter the IP address to get location information: ")
    while not ip_address:
        ip_address = input("Please enter a valid IP address: ")

    # Taking file name input from the user
    dosyaAdi = input("Enter the file name to save the report (or press Enter to skip): ")

    try:
        adres = f"http://ip-api.com/json/{ip_address}"
        sonuc = requests.get(adres, verify=False).json()

        # Print location information
        print("[+]City:", sonuc.get('city'))
        print("[+]Country:", sonuc.get('country'))
        print("[+]Time Zone:", sonuc.get('timezone'))

        if dosyaAdi:
            # Save to file if a file name is provided
            raporIcerik = "[+]City: " + str(sonuc.get('city')) + "\n"
            raporIcerik += "[+]Country: " + str(sonuc.get('country')) + "\n"
            raporIcerik += "[+]Time Zone: " + str(sonuc.get('timezone')) + "\n"

            rapor = open(dosyaAdi, "a")
            rapor.write(raporIcerik)
            rapor.close()

    except Exception as e:
        print(f"Error: {e}")
        print("Please check the IP address and try again.")



# Call the function
IP2Location()
