from seleniumwire import webdriver
from seleniumwire.utils import decode as decodesw
import seleniumwire.undetected_chromedriver as uc
import json

#beed ti xplore more on selenium and chromedriver


#to get urls that run on website
def show_request_urls(driver, target_url):
  driver.get(target_url)
  urls = []
  for request in driver.requests:
    urls.append({"url":request.url})
  return urls

def main():
  chrome_options = uc.ChromeOptions()
  driver = uc.Chrome(options=chrome_options, seleniumwire_options={"disable_encoding": True})
  target_url = "https://www.senheng.com.my/all-products/home-entertainment.html"
#   target_url = "https://www.jakartanotebook.com/pc-and-laptop"

  urls = show_request_urls(driver, target_url)

  for url in urls:
    print(url)

if __name__ == "__main__":
  main()