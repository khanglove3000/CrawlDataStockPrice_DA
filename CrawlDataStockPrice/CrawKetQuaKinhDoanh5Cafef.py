from selenium import webdriver
from SaveFileRawData import SaveFileDataCSV
import pandas as pd
import time

from selenium.webdriver.chrome.options import Options 
option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(executable_path="D:\chromedriver")

class ThongTinTaiChinh:
    def __init__(self, symbol, url, filename):
        self.symbol = symbol
        self.url = url
        self.filename = filename
        self.DataExceptlists = ['Lãi gộp từ HĐ tài chính', '''Lãi gộp từ HĐ SX-KD chính
                                                    Lãi gộp từ HĐ tài chính
                                                    Lãi gộp từ HĐ khác''', 
                                                    ''''
                                                    "Lãi gộp từ HĐ SX-KD chính
                                                    Lãi gộp từ HĐ tài chính
                                                    Lãi gộp từ HĐ khác"
                                                    ''']
    # Chi so chi tieu
    # Begin
    def chisochitieu(self):
    
        driver.get(self.url)
        i = 2
        bunttonQuy = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[1]/div[1]/a[1]"
        thontintaichinh_Quy = driver.find_elements_by_xpath(bunttonQuy)[0] # craw data theo quy
        thontintaichinh_Quy.click()
        time.sleep(1)

        chitieukehoach = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[3]/div[1]/table/thead/tr/th"
        chitieutaichinh = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[3]/div[1]/table/tbody/tr/td[1]"
        column1 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[3]/div[1]/table/tbody/tr/td[2]"
        column2 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[3]/div[1]/table/tbody/tr/td[3]"
        column3 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[3]/div[1]/table/tbody/tr/td[4]"
        column4 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[3]/div[1]/table/tbody/tr/td[5]"

        datachitieukehoach = [data.text for data in driver.find_elements_by_xpath(chitieukehoach)]
        datachitieutaichinh = [data.text for data in driver.find_elements_by_xpath(chitieutaichinh)]
        datacolumn1 = [data.text for data in driver.find_elements_by_xpath(column1)]
        datacolumn2 = [data.text for data in driver.find_elements_by_xpath(column2)]
        datacolumn3 = [data.text for data in driver.find_elements_by_xpath(column3)]
        datacolumn4 = [data.text for data in driver.find_elements_by_xpath(column4)]

        data = {
            datachitieukehoach[0]: datachitieutaichinh,
            datachitieukehoach[1]: datacolumn1,
            datachitieukehoach[2]: datacolumn2,
            datachitieukehoach[3]: datacolumn3,
            datachitieukehoach[4]: datacolumn4,
            'Symbol': self.symbol   
        }
        SaveFileDataCSV(self.filename, data)
        driver.close()    

        # End

    # Chi so tai chinh : KQKD, TaiSan theo Name
    def Nam(self):
        
        driver.get(self.url)
        i = 2
        bunttonNam = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[1]/div[1]/a[2]"
        thontintaichinh_Nam = driver.find_elements_by_xpath(bunttonNam)[0] # craw data thong tin tai chinh theo nam
        thontintaichinh_Nam.click()
        time.sleep(1)

        chitieukehoach = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[2]/table/tbody/tr[1]/th"
        chitieutaichinh = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]"
        column1 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[2]"
        column2 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[3]"
        column3 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[4]"
        column4 = "/html/body/form/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div[10]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]"

        datachitieukehoach = [data.text for data in driver.find_elements_by_xpath(chitieukehoach)]
        datachitieutaichinh = [data.text for data in driver.find_elements_by_xpath(chitieutaichinh)]
        datacolumn1 = [data.text for data in driver.find_elements_by_xpath(column1)]
        datacolumn2 = [data.text for data in driver.find_elements_by_xpath(column2)]
        datacolumn3 = [data.text for data in driver.find_elements_by_xpath(column3)]
        datacolumn4 = [data.text for data in driver.find_elements_by_xpath(column4)]

        data = {
            datachitieukehoach[0]: datachitieutaichinh,
            datachitieukehoach[1]: datacolumn1,
            datachitieukehoach[2]: datacolumn2,
            datachitieukehoach[3]: datacolumn3,
            datachitieukehoach[4]: datacolumn4,
            'Symbol': self.symbol   
        }
        SaveFileDataCSV(self.filename, data)
        driver.close()    
  
