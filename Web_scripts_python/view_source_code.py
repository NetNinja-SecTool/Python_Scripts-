import requests

#View HTML Source Code:

def view_html_source(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_source = response.text
            print("HTML Source Code:")
            print(html_source)
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during request: {e}")
      
if __name__ == "__main__":

    website_url = input("Enter the website url : ")
    view_html_source(website_url)

