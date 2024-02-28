import requests

def view_url_extensions(url):
    extensions = url.split(".")[-1]
    print("URL Extensions:", extensions)


if __name__ == "__main__":

    website_url = input("Enter the website url : ")

    view_url_extensions(website_url)
  
