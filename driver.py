from selenium import webdriver



def get_driver():
    service = webdriver.chrome.service.Service('./chromedriver')
    service.start()  
    options = webdriver.ChromeOptions()                
    options.add_argument('--headless')
    options = options.to_capabilities()
    driver = webdriver.Remote(service.service_url, options)
    return driver
