from selenium import webdriver
from selenium.common import exceptions  
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options 

options = webdriver.ChromeOptions()
options.add_argument('headless')

def CrawlDatLenhChiTiet(driver, ItemPrice, symbol, filename):
    ngays = [data.text for data in driver.find_elements_by_xpath('''//td[@class="Item_DateItem"]''')]
    thaydoi = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][1]''')]
    solenhmua = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][2]''')]
    khoiluongdatmua = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][3]''')]
    KLTB1lenhmua = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][4]''')]
    solenhdatban = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][5]''')]
    khoiluongdatban = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][6]''')]
    KLTB1lenhban = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][7]''')]
    chenhlechlenhmuavaban = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][8]''')]

    data = {
    'ngay': ngays,
    'thaydoi': thaydoi,
    'solenhmua': solenhmua,
    'khoiluongdatmua': khoiluongdatmua,
    'KLTB1lenhmua': KLTB1lenhmua,
    'solenhdatban': solenhdatban,
    'khoiluongdatban': khoiluongdatban,
    'KLTB1lenhban': KLTB1lenhban,
    'chenhlechlenhmuavaban': chenhlechlenhmuavaban,
    'symbol': symbol
    }
    list_dataframe = pd.DataFrame.from_dict(data)
    filedata = filename
    with open(filedata, 'a') as f:
                list_dataframe.to_csv(f, mode='a', header=f.tell()==0)

def CrawlThongKeDatLenh(symbol, url, filename):
    driver = webdriver.Chrome(executable_path="D:\chromedriver",options=options)
    driver.get(url)
    i = 2
    selects = """//*[@id="content"]/div/div/a[1]"""
    urlhistorydata = driver.find_elements_by_xpath(selects)[0]
    urlhistorydata.click()
    time.sleep(3)
    selects = """//*[@id="ctl00_ContentPlaceHolder1_aTKL"]"""
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
                CrawlDatLenhChiTiet(driver, ItemPrice, symbol, filename)
            except:
                ItemPrice = 'Item_Price'
                CrawlDatLenhChiTiet(driver, ItemPrice, symbol, filename)
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