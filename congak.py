import seleniumwire.undetected_chromedriver as uc

## Chrome Options
chrome_options = uc.ChromeOptions()

## Create Chrome Driver
driver = uc.Chrome(
    options=chrome_options,
    seleniumwire_options={}
)

driver.get('https://www.senheng.com.my/all-products/home-entertainment.html')