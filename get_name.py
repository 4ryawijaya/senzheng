from bs4 import BeautifulSoup
import requests

#parsing the html structure
def get_data(url, headers):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.prettify() 

def get_name():
   pass

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    url = "https://www.senheng.com.my/all-products/home-entertainment.html"
    urls = get_data(url, headers)

    print(urls)

if __name__ == "__main__":
  main()


