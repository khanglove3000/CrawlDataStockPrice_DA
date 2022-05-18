from selenium import webdriver
from selenium.common import exceptions  
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options 

option = webdriver.ChromeOptions()
option.add_argument('headless')

def CrawlDataHistory(driver, ItemPrice, symbol, filename):
        ngays = [data.text for data in driver.find_elements_by_xpath('''//td[@class="Item_DateItem"]''')]
        giadieuchinh = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][1]''')]
        giadongcua = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][2]''')]
        giathaydoi = [data.text for data in driver.find_elements_by_xpath('''//*[@class="Item_ChangePrice"]/span''')]
        KL = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][3]''')]
        GT = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][4]''')]
        giamocua = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][6]''')]
        giacaonhat = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][7]''')]
        giathapnhat = [data.text for data in driver.find_elements_by_xpath('''//*[@class="'''+str(ItemPrice)+'''"][8]''')]
    
        data = {
            'ngay': ngays,
            'giadieuchinh': giadieuchinh,
            'giadongcua': giadongcua,
            'giathaydoi': giathaydoi,
            'KL': KL,
            'GT': GT,
            'giamocua': giamocua,
            'giacaonhat': giacaonhat,
            'giathapnhat': giathapnhat,
            'symbol': symbol
        }
        list_dataframe = pd.DataFrame.from_dict(data)
        filedata = filename
        with open(filedata, 'a') as f:
                    list_dataframe.to_csv(f, mode='a', header=f.tell()==0)
            
def CrawlDataKQKD(symbol, url, filename):
    driver = webdriver.Chrome(executable_path="D:\chromedriver")
    driver.get(url)
    i = 2
    selects = """//*[@id="divHoSoCongTyAjax"]/table/tbody/tr[11]/td/a""" # chon nut xem them
    urlhistorydata = driver.find_elements_by_xpath(selects)[0] # chon nut xem them
    urlhistorydata.click() # chon nut xem them
    time.sleep(1) 

    selectcontent = """/html/body/form/div[3]/div/div/div/div[2]/div[2]/div[9]/div[2]/table/tbody/tr/td[1]"""
    selectQui1 = "/html/body/form/div[3]/div/div/div/div[2]/div[2]/div[9]/div[2]/table/tbody/tr/td[2]"
    selectQui2 = "/html/body/form/div[3]/div/div/div/div[2]/div[2]/div[9]/div[2]/table/tbody/tr/td[3]"
    selectQui3 = "/html/body/form/div[3]/div/div/div/div[2]/div[2]/div[9]/div[2]/table/tbody/tr/td[4]"
    selectQui4 = "/html/body/form/div[3]/div/div/div/div[2]/div[2]/div[9]/div[2]/table/tbody/tr/td[5]"
    
    noidung = [data.text for data in driver.find_elements_by_xpath(selectcontent)]
    Qui1 = [data.text for data in driver.find_elements_by_xpath(selectQui1)]
    Qui2 = [data.text for data in driver.find_elements_by_xpath(selectQui2)]
    Qui3 = [data.text for data in driver.find_elements_by_xpath(selectQui3)]
    Qui4 = [data.text for data in driver.find_elements_by_xpath(selectQui4)]
    
    data = {
        'noidung': noidung,
        'Qui1': Qui1,
        'Qui2': Qui2,
        'Qui3': Qui3,
        'Qui4': Qui4,
        'Symbol': symbol
    }
    list_dataframe = pd.DataFrame.from_dict(data)
    filedata = filename
    with open(filedata, 'a', encoding='UTF8') as f:
                list_dataframe.to_csv(f, mode='a', header=f.tell()==0)
    # while True:
    #     try: 
    #         time.sleep(1)
    #         try:
    #             ItemPrice = 'Item_Price10'
    #             CrawlDataHistory(driver, ItemPrice, symbol, filename)
    #         except:
    #             ItemPrice = 'Item_Price1'
    #             CrawlDataHistory(driver, ItemPrice, symbol, filename)
            
    #         try:
    #             # page2
    #             try:
    #                 time.sleep(1)
    #                 nextpage = driver.find_elements_by_xpath(""".//td/a[@href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','""" + str(i) + """')"]""")[0]
    #                 nextpage.click()

    #             # page1   
    #             except:
    #                 time.sleep(1)
    #                 nextpage = driver.find_elements_by_xpath(""".//td/a[@href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','""" + str(i) + """')"]""")[0]
    #                 nextpage.click()
                   
    #         except IndexError:
    #             break
    #         i = i + 1
    #     except exceptions.StaleElementReferenceException:
    #             pass
    driver.close()