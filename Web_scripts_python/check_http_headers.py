import request 

def view_http_headers(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            headers = response.headers
            print("HTTP Headers:")
            for key, value in headers.items():
                print(f"{key}: {value}")
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during request: {e}")

if __name__ == "__main__":

    website_url = input("Enter the website url : ")
    view_http_headers(website_url)
   
