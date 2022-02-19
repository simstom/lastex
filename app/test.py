from lib2to3.pgen2 import driver
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# options.add_argument('window-size=1200x600')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# browser = webdriver.Chrome(chrome_options=options)
#chrome드라이버가 PATH 환경변수 설정이 되어있지 않다면 executable_path 옵션으로 chromedriver 위치 지정
print("---------------------------------1")
driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/src/chrome/chromedriver")
# /usr/src/chrome
print("-----------------------------------------------2")
driver.get("http://www.python.org")
# assert "Python" in self.driver.title
print("-----------------------------------------------3")
print(driver.title)
print("-----------------------------------------------4")
driver.close()

# url = "http://google.com"

# browser.get(url)
# browser.save_screenshot("Website.png")
# browser.quit()