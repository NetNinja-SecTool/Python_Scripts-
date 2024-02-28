import requests


def sitemapxml_available(url):
    url += "/sitemap.xml"
    try:
        sonuc = requests.get(url, verify=True)
        sonuc.raise_for_status()

        if sonuc.status_code == 200:
            print(f"[+] Sitemap.xml is available on {url}")
        else:
            print(f"[-] Sitemap.xml isn't available on {url}")
    except requests.RequestException as e:
        if "404" in str(e):
            print(f"[-] Sitemap.xml not found on {url}")
        else:
            print(f"Error: {e}")
            print(f"[-] Failed to check Sitemap.xml on {url}")

if __name__ == "__main__":
    website_url = input("Enter the URL: ")
    sitemapxml_available(website_url)
