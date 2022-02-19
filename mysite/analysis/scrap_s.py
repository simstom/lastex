from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
# from lib2to3.pgen2 import driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# # options.add_argument('window-size=1200x600')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# # browser = webdriver.Chrome(chrome_options=options)
# #chrome드라이버가 PATH 환경변수 설정이 되어있지 않다면 executable_path 옵션으로 chromedriver 위치 지정
# print("---------------------------------1")
# driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/src/chrome/chromedriver")
# # /usr/src/chrome
# print("-----------------------------------------------2")
# driver.get("http://www.python.org")
# # assert "Python" in self.driver.title
# print("-----------------------------------------------3")
# print(driver.title)
# print("-----------------------------------------------4")
# driver.close()

# url = "http://google.com"

# browser.get(url)
# browser.save_screenshot("Website.png")
# browser.quit()


class Scrap:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('window-size=1200x600')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        # chromedriver_autoinstaller.install()  
        # # Check if the current version of chromedriver exists
        # #   and if it doesn't exist, download it automatically,
        # #   then add chromedriver to path
        # self.driver = webdriver.Chrome()
        # /usr/local/bin/chromedriver
        # s=Service('./chromedriver')
        # self.driver = webdriver.Chrome("./")
        # browser = webdriver.Chrome(chrome_options=options)
        #chrome드라이버가 PATH 환경변수 설정이 되어있지 않다면 executable_path 옵션으로 chromedriver 위치 지정
        # driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/src/chrome/chromedriver")
        # /usr/src/chrome
        # print("---------------------------------1")

        # # self.driver = webdriver.Chrome(chrome_options=options, executable_path="/srv/docker-server/chrome/chromedriver")
        # # /srv/docker-server/chrome
        
        
        # print("-----------------------------------------------2")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())



        

    def scrap(self , flag = False):
        if flag:
            print("---------------------------------1")
            # options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            # # options.add_argument('window-size=1200x600')
            # options.add_argument('--no-sandbox')
            # options.add_argument('--disable-dev-shm-usage')

            driver = webdriver.Chrome(chrome_options=self.options, executable_path="/usr/local/bin/chromedriver")
            # # /srv/docker-server/chrome ==>  /usr/local/bin/
        
        
            # print("-----------------------------------------------2")
            # driver = webdriver.Chrome(ChromeDriverManager().install())        
            driver.get("http://www.python.org")
            # assert "Python" in self.driver.title
            print("============================title")
            print(driver.title)
            html = driver.page_source
            title = driver.title
            # print(html)
            print("============================end")
            driver.close()
            # title = "값을 가지고 올수없어요.-----------"
        return html

if __name__ == "__main__":
    start_scrap = Scrap()
    start_scrap.scrap(True)
    print("---------------------------처리 끝--------------------")