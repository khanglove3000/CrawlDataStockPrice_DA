from selenium import webdriver
from selenium.common import exceptions  
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options 

options = webdriver.ChromeOptions()
options.add_argument('headless')

def CrawlGiaoDichNgoaiKhoiChiTiet(driver, ItemPrice, symbol, filename):
    ngays = [data.text for data in driver.find_elements_by_xpath('''//td[@class="Item_DateItem"]''')]
    KLDichRong = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][1]''')]
    GiaTriGiaoDichRong = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][2]''')]
    ThayDoi = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][3]''')]
    KhoiLuongMua = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][4]''')]
    GiaTriMua = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][5]''')]
    KhoiLuongBan = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][6]''')]
    GiaTriBan = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][7]''')]

    data = {
    'ngay': ngays,
    'KLDichRong': KLDichRong,
    'GiaTriGiaoDichRong': GiaTriGiaoDichRong,
    'ThayDoi': ThayDoi,
    'KhoiLuongMua': KhoiLuongMua,
    'GiaTriMua': GiaTriMua,
    'KhoiLuongBan': KhoiLuongBan,
    'GiaTriBan': GiaTriBan,
    'symbol': symbol
    }
    list_dataframe = pd.DataFrame.from_dict(data)
    filedata = filename
    with open(filedata, 'a') as f:
                list_dataframe.to_csv(f, mode='a', header=f.tell()==0)

def CrawlGiaoDichNgoaiKhoi(symbol, url, filename):
    driver = webdriver.Chrome(executable_path="D:\chromedriver",options=options)
    driver.get(url)
    i = 2
    selects = """//*[@id="content"]/div/div/a[1]"""
    urlhistorydata = driver.find_elements_by_xpath(selects)[0]
    urlhistorydata.click()
    time.sleep(3)
    selects = """//*[@id="ctl00_ContentPlaceHolder1_aNDTNG"]"""
    urlhistorydata = driver.find_elements_by_xpath(selects)[0]
    urlhistorydata.click()
    driver.get(driver.current_url)
    time.sleep(5)
    ItemPrice = 'Item_Price'
    while True:
        try: 
            time.sleep(1)
            try:
                ItemPrice = 'Item_Price'
                CrawlGiaoDichNgoaiKhoiChiTiet(driver, ItemPrice, symbol, filename)
            except:
                ItemPrice = 'Item_Price'
                CrawlGiaoDichNgoaiKhoiChiTiet(driver, ItemPrice, symbol, filename)
            try:
                # page2
                try:
                    time.sleep(1)
                    nextpage = driver.find_elements_by_xpath(""".//td/a[@href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','""" + str(i) + """')"]""")[0]
                    nextpage.click()

                # page1   
                except:
                    time.sleep(1)
                    nextpage = driver.find_elements_by_xpath(""".//td/a[@href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','""" + str(i) + """')"]""")[0]
                    nextpage.click()
                   
            except IndexError:
                break
            i = i + 1
        except exceptions.StaleElementReferenceException:
                pass
    driver.close()