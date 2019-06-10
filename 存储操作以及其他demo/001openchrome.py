from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.google.com")
i=0
while i<10:
    browser.get("https://www.google.com")
    i+=1;

print(browser.current_url)