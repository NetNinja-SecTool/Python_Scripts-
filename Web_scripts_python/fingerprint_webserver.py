import requests

def find_web_server_type(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            server_header = response.headers.get('Server', '')
            print(f"Web Server Type: {server_header}")
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during request: {e}")


def find_web_server_version(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            server_header = response.headers.get('Server', '')
            x_powered_by_header = response.headers.get('X-Powered-By', '')
            print(f"Web Server Version: {server_header}")
            print(f"X-Powered-By: {x_powered_by_header}")
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during request: {e}")


if __name__ == "__main__":

    website_url = input("Enter the website url:")
    find_web_server_type(website_url)
    find_web_server_version(website_url)



#http://testphp.vulnweb.com/
