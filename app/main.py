from unicodedata import name
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time






class Scrap:

    def __init__(self):
        # chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
        print("--------------------------------------------------2")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        time.sleep(5)
        
        print("--------------------------------------------------2")
        # self.driver = webdriver.Chrome()
        # /usr/local/bin/chromedriver
        # s=Service('./chromedriver')
        # self.driver = webdriver.Chrome("./chrome/chromedriver")
        # self.driver = webdriver.Chrome()
        print(self.driver)
        print("---------------------------------------------3")


        

    def scrap(self , flag = False):
        if flag:        
            self.driver.get("http://www.python.org")
            # assert "Python" in self.driver.title
            print(self.driver.title)
            html = self.driver.page_source
            for i in range(5):
                title = self.driver.title
            # print(html)
            self.driver.close()
        return title

if __name__ == "__main__":
    print("시작하고 있어요----------------------------------------------------1--")
    start_scrap = Scrap()

    print("시작하고 있어요----------------------------------------------------55--")

    return_title = start_scrap.scrap(True)
    print(" 마지막 값입니다. =============> ", return_title)